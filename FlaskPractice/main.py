import json
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
	number = SelectField('有幾項呢', choices=[('1','1 項'), ('2','2 項')])
	item = StringField('Name')
	add = SubmitField(label='加入')
	submit = SubmitField('幫我選一個吧')

# 神選之物
@app.route('/DiffToChoice', methods=['GET', 'POST'])
def DiffToChoice():
	form = TestForm()

	qu=[]
	itemss = form.item.data

	if request.method == 'POST':
		if request.form['submit'] == 'Do':
			qu.append(itemss)
		elif request.form['submit'] == 'NotDo':
			return render_template('ToGoogle.html', form=form)
		else:
			pass
	elif request.method == 'GET':
		return render_template('DiffToChoice.html', form=form)



@app.route('/ToGoogle')
def ToGoogle():
	import webbrowser
	webbrowser.open('https://google.com')
	return render_template('ToGoogle.html')




if __name__ == '__main__':
	app.run(debug=True)










