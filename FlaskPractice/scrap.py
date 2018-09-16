from bs4 import BeautifulSoup
import requests
import urllib3
import http.cookiejar as cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://portal.stust.edu.tw/examseat/login.aspx")

br.select_form(nr=0)
br.form['username'] = 'username'
br.form['password'] = 'password.'
br.submit()

print (br.response().read())

# login = requests.get('https://portal.stust.edu.tw/examseat/login.aspx').text
# # print(login.status_code)

# soup = BeautifulSoup(login, 'lxml')

# source = soup.find('table')

# inputf = table.tdbody.tr.td.input.text

# print(inputf)


# >>> BeautifulSoup(html, 'html.parser').find("div",{"id":"cntPos"}).find("table",{"class":"cntTb"}).tbody.find_all("tr")[1].find("td",{"class":"cntBoxGreyLnk"}) is None
# True
# >>> BeautifulSoup(html, 'lxml').find("div",{"id":"cntPos"}).find("table",{"class":"cntTb"}).tbody.find_all("tr")[1].find("td",{"class":"cntBoxGreyLnk"}) is None
# False