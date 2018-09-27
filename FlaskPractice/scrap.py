from bs4 import BeautifulSoup
import requests

def login():
	loginPage = requests.get('https://portal.stust.edu.tw/examseat/login.aspx').text
	# print(login.status_code)

	soup = BeautifulSoup(loginPage, 'lxml')

	match = soup.find_all('td', align='center')

	print(match)

def examResults():
	with open('ExamResults.htm', encoding = 'utf8') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

	# Get Table of Exam Information
	for seat in soup.find_all('table', id="DataGrid1"):
		trrr = seat.find_all('tr')
		print(trrr)
			# for trr in seat.tr:
			# 	print(trr)


examResults()
