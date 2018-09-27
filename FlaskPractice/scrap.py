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
	table = soup.find('table', id='DataGrid1')
	rows = table.find_all('tr')

	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		# Get rid of empty values
		data.append([ele for ele in cols if ele])
	print(data)
	
examResults()
