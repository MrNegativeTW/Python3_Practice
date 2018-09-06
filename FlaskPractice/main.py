import json
from flask import Flask, render_template, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

class TestForm(FlaskForm):
	number = SelectField('有幾項呢', choices=[('1','1 項'), ('2','2 項')])
	item = StringField('Name')
	add = SubmitField('加入')
	submit = SubmitField('幫我選一個吧')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a83c51c8b7fc804eb395d7c1d753fa28'

# Index
@app.route('/')
def hello():
	return render_template('index.html')

# 神選之物
@app.route('/DiffToChoice', methods=['GET', 'POST'])
def DiffToChoice():
	form = TestForm()
	qu=[]
	itemss = form.item.data
	if request.method == 'POST':
		qu.append(itemss)

	return render_template('DiffToChoice.html', form=form)



@app.route('/ToGoogle')
def ToGoogle():
	import webbrowser
	webbrowser.open('https://google.com')
	return render_template('ToGoogle.html')




if __name__ == '__main__':
	app.run(debug=True)










