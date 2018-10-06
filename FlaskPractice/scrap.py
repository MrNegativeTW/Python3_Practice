from bs4 import BeautifulSoup
import requests

# Let me in
def login():
	# Let's get some exam information, ready?
	with requests.Session() as s:
		
		# -----First Step - Login exam seat system-----
		page = s.get('https://portal.stust.edu.tw/examseat/login.aspx')
		soup = BeautifulSoup(page.content, 'lxml')

		# Username and password to login
		payload_loginPage = {
			'txtStud_No': '4A6F0072', 
			'txtPasswd': 'wow',
			'Button1': '登入'
		}

		# For asp.net
		payload_loginPage["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
		payload_loginPage["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
		payload_loginPage["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
		s.post('https://portal.stust.edu.tw/examseat/login.aspx', data=payload_loginPage)

		
		# -----Second Step - Select exam type-----
		page = s.get('https://portal.stust.edu.tw/examseat/Default.aspx')
		# Select that fucking type of exam
		payload_examType = {
			'exam_type': 'examTypeValue', 
			'Button1': '開始查詢'
		}
		# For asp.net
		payload_examType["__VIEWSTATE"] = soup.select_one("#__VIEWSTATE")["value"]
		payload_examType["__VIEWSTATEGENERATOR"] = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
		payload_examType["__EVENTVALIDATION"] = soup.select_one("#__EVENTVALIDATION")["value"]
		s.post('https://portal.stust.edu.tw/examseat/Default.aspx', data=payload_examType)


		# -----Third Step - Now we got what we need-----
		global openPage
		openPage = s.get('http://portal.stust.edu.tw/examseat/ShowResult.aspx').text
		# print(openPage.text)

login()

# Get Exam Result
def examResults():
	# with open('ExamResultOriginal.htm', encoding = 'utf8') as html_file:
	soup = BeautifulSoup(openPage, 'lxml')

	# Empty list
	data = []

	# Find Target table
	table = soup.find('table', id='DataGrid1')
	rows = table.find_all('tr')

	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		# Get rid of empty values
		data.append([ele for ele in cols if ele])


	date = []
	period = []
	timeOfExam = []
	room = []
	row = []
	col = []
	subject = []
	for each in data:
		date.append(each[0])
		period.append(each[1])
		timeOfExam.append(each[2])
		room.append(each[3])
		row.append(each[4])
		col.append(each[5])
		subject.append(each[6])

	lengh = len(date)
	print(date)
	print(period)
	print(timeOfExam)
	print(room)
	print(row)
	print(col)
	print(subject)
	
examResults()
