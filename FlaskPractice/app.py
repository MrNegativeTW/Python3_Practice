from flask import Flask, render_template, url_for, flash, request

# Custom WTFroms
from forms import DiffToChoiceForm, GasPricePerKmForm, BeautifulExamForm, AutoExamForm, WorkingForm

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
	return render_template('BeautifulExam.html', form=form)

# 自動考試 / AutoExam
@app.route('/AutoExam', methods=['GET', 'POST'])
def AutoExam():
	form = AutoExamForm()
	return render_template('AutoExam.html', form=form)

# 待發展 / Working
@app.route('/Working', methods=['GET', 'POST'])
def Working():
	form = WorkingForm()
	if form.validate_on_submit():
		return render_template('Working.html', form=form, wow=wowww)
	return render_template('Working.html', form=form)






if __name__ == '__main__':
	app.run(debug=True)
