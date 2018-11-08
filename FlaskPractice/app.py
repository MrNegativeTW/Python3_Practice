from flask import Flask, render_template, url_for, flash, request, redirect
# -----Custom WTFroms-----
from forms import DiffToChoiceForm, GasPricePerKmForm, BeautifulExamForm, AutoExamForm, UpperForm

# -----For Exam Service-----
from bs4 import BeautifulSoup
import requests
from scrap import login, examResults, data, date, period, timeOfExam, room, rowsss, col, subject, dataLengh






# App Start
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a83c51c8b7fc804eb395d7c1d753fa28'





# Index
@app.route('/')
def hello():
	return render_template('index.html')





# 神選之物 / DiffToChoice
@app.route('/DiffToChoice', methods=['GET', 'POST'])
def DiffToChoice():
	import random
	form = DiffToChoiceForm()

	qu=[]
	itemssOne = form.itemOne.data
	itemssTwo = form.itemTwo.data

	if request.method == 'GET':
		return render_template('DiffToChoice.html', form=form)
	elif request.method == 'POST':
		qu.clear()
		qu.append(itemssOne)
		qu.append(itemssTwo)
		ans = random.choice(qu)
		return render_template('DiffToChoice.html',title='油耗計算', form=form, ans=ans)





# ToGoogle
@app.route('/ToGoogle')
def ToGoogle():
	import webbrowser
	webbrowser.open('https://google.com')
	return render_template('ToGoogle.html', title='ToGoogle')





# 油耗計算 / GasPricePerKm
@app.route('/GasPricePerKm', methods=['GET', 'POST'])
def GasPricePerKm():
	form = GasPricePerKmForm()

	if form.validate_on_submit():
		x = float(form.mileage.data)
		y = float(form.oil.data)
		result = x / y
		results = int(result)
		return render_template('GasPricePerKm.html',title='油耗計算', form=form, result=results)

	return render_template('GasPricePerKm.html',title='油耗計算', form=form)





# 漂亮的考試時間 / BeautifulExam
@app.route('/BeautifulExam', methods=['GET', 'POST'])
def BeautifulExam():
	form = BeautifulExamForm()
# --DELETE THESE CODE----------------------------------------------------------------------
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
# ---------------------------------------------------
	return render_template('BeautifulExam.html', 
		form=form,
		data=data, 
		dataLengh=dataLengh, 
		date=date, 
		preiod=period, 
		timeOfExam=timeOfExam, 
		room=room, 
		row=rowsss, 
		col=col, 
		subject=subject
	)

	if form.validate_on_submit():
		usernameb = form.usernamef.data
		passwordb = form.passwordf.data

		login(usernameb, passwordb)
		examResults()

		return render_template('BeautifulExam.html', 
		form=form, 
		data=data, 
		dataLengh=dataLengh, 
		date=date, 
		preiod=period, 
		timeOfExam=timeOfExam, 
		room=room, 
		row=rowsss, 
		col=col, 
		subject=subject
		)

	# return render_template('BeautifulExam.html', 
	# 	form=form, 
	# 	data=data, 
	# 	dataLengh=dataLengh, 
	# 	date=date, 
	# 	preiod=period, 
	# 	timeOfExam=timeOfExam, 
	# 	room=room, 
	# 	row=rowsss, 
	# 	col=col, 
	# 	subject=subject
	# 	)






























































# 自動考試 / AutoExam
@app.route('/AutoExam', methods=['GET', 'POST'])
def AutoExam():
	form = AutoExamForm()
	return render_template('AutoExam.html', form=form)





# 大小寫 / Upper
@app.route('/Upper', methods=['GET', 'POST'])
def Upper():
	form = UpperForm()
	if form.validate_on_submit():
		text = form.textin.data
		if text == '0':
			return redirect('../')
		# Split sentences/text by dot, save in otext / 使用句點分割句子，存於 otext
		otext = text.split('. ')
		# Remove dot and space / 移除句首和句尾的空格和句點
		trimmed = [
			sentence.strip()
			for sentence in otext
			]
		# Change first letter to upper / 句首變大寫
		upper = [
			sentence[0].upper() + sentence[1:]
			for sentence in trimmed
			]
		# Add dot and space to final results / 加入句點和空格
		results = '. '.join(upper)
		# Print Final Result / 輸出最後結果
		# print(results)
		return render_template('Upper.html', form=form, results=results)

	return render_template('Upper.html', form=form)






if __name__ == '__main__':
	app.run(debug=True)