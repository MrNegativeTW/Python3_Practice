import json, random
from flask import Flask, render_template, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a83c51c8b7fc804eb395d7c1d753fa28'

# Index
@app.route('/')
def hello():
	return render_template('index.html')

class TestForm(FlaskForm):
	number = SelectField('有幾個東西讓你選擇障礙呢：', choices=[('2','2 項'), ('3','3 項')])
	itemOne = StringField('第一項')
	itemTwo = StringField('第二項')
	# add = SubmitField(label='加入')
	submit = SubmitField('神啊 幫我選一個')

# 神選之物
@app.route('/DiffToChoice', methods=['GET', 'POST'])
def DiffToChoice():
	form = TestForm()

	qu=[]
	itemssOne = form.itemOne.data
	itemssTwo = form.itemTwo.data

	if request.method == 'GET':
		return render_template('DiffToChoice.html', form=form)
	elif request.method == 'POST':
		qu.append(itemssOne)
		qu.append(itemssTwo)
		ans = random.choice(qu)
		# return(ans)
		return render_template('DiffToChoice.html', form=form)

@app.route('/ToGoogle')
def ToGoogle():
	import webbrowser
	webbrowser.open('https://google.com')
	return render_template('ToGoogle.html')




if __name__ == '__main__':
	app.run(debug=True)










