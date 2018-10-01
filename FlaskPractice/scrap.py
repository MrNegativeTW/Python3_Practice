from bs4 import BeautifulSoup
import requests

def login():
	loginPage = requests.get('https://portal.stust.edu.tw/examseat/login.aspx').text
	# print(login.status_code)

	soup = BeautifulSoup(loginPage, 'lxml')

	match = soup.find_all('td', align='center')

	print(match)

def examResults():
	with open('ExamResultOriginal.htm', encoding = 'utf8') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

	# Get Table of Exam Information
	data = []

	# Find Target
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

	print(date)
	print(period)
	print(timeOfExam)
	print(room)
	print(row)
	print(col)
	print(subject)
	
examResults()
