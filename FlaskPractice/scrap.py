from bs4 import BeautifulSoup
import requests
import urllib.request # S3


# 登入系統
def login():
	with requests.Session() as s:
		'''
		Step. 1
		Get in to Exam seat system
		'''
		page = s.get('https://portal.stust.edu.tw/examseat/login.aspx')
		soup = BeautifulSoup(page.content, 'lxml')

		# Basic Login Information
		payload_loginPage = {
			'txtStud_No': username, 
			'txtPasswd': password,
			'Button1': '登入'
		}

		# For asp.net
		# payload_loginPage["txtStud_No"] = usernameb
		# payload_loginPage["txtPasswd"] = passwordb
		payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
		payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
		payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]

		# POST data above to login page.
		s.post('https://portal.stust.edu.tw/examseat/login.aspx', data=payload_loginPage)


		'''
		Step. 2
		Select Exam Type
		'''
		page = s.get('https://portal.stust.edu.tw/examseat/Default.aspx')

		# Select Type
		payload_examType = {
			'exam_type': 'examTypeValue', 
			'Button1': '開始查詢'
		}

		# For asp.net
		payload_examType["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
		payload_examType["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
		payload_examType["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]

		# POST data above to type select page
		s.post('https://portal.stust.edu.tw/examseat/Default.aspx', data=payload_examType)

		'''
		Step. 3
		Get Result Page
		The Question is, python GET the page what we need to fast, should GET after page complete loaded.
		'''
		global openPage
		openPage = s.get('http://portal.stust.edu.tw/examseat/ShowResult.aspx').text

		print(openPage)

# login()



# 取得考試座位資訊
def examResults():
	# with open('ExamResultOriginal.htm', encoding = 'utf8') as html_file:
	with open('ExamResultOriginal2.html', encoding = 'utf8') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

	# soup = BeautifulSoup(openPage, 'lxml')

	# Empty list, just... global it
	global data
	data = []

	# Find Target table
	table = soup.find('table', id='DataGrid1')
	rows = table.find_all('tr')

	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		# Get rid of empty values
		data.append([ele for ele in cols if ele])

	# Global these empty lists
	global date
	global period
	global timeOfExam
	global room
	global rowsss
	global col
	global subject

	date = []
	period = []
	timeOfExam = []
	room = []
	rowsss = []
	col = []
	subject = []

	for each in data:
		date.append(each[0])
		period.append(each[1])
		timeOfExam.append(each[2])
		room.append(each[3])
		rowsss.append(each[4])
		col.append(each[5])
		subject.append(each[6])

	global dataLengh
	dataLengh = len(date)

	# Debug
	print(date)
	print(period)
	print(timeOfExam)
	print(room)
	print(rowsss)
	print(col)
	print(subject)
	
examResults()
