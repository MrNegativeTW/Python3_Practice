from bs4 import BeautifulSoup
import requests

def login():
	loginPage = requests.get('https://portal.stust.edu.tw/examseat/login.aspx').text
	# print(login.status_code)

	soup = BeautifulSoup(loginPage, 'lxml')

	match = soup.find_all('td', align='center')

	print(match)

def examResults():
	with open('ExamResults.htm') as html_file:
		soup = BeautifulSoup(html_file, 'lxml')

	for seat in soup.find_all('tr'):
		time = seat.tr

	print(time)

examResults()


