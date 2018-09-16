from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange, Regexp

# 神選之物
class DiffToChoiceForm(FlaskForm):
	number = SelectField(
		'選擇障礙數量：（開發中）', 
		choices=[('2','2 項'), ('3','3 項')
		])
	itemOne = StringField('第一項')
	itemTwo = StringField('第二項')
	# add = SubmitField(label='加入')
	submit = SubmitField('神啊 幫我選一個')

# 油耗計算 / GasPricePerKm
class GasPricePerKmForm(FlaskForm):
	mileage = StringField(
				'Trip 里程數',
				validators=[
					DataRequired(),
					Regexp(regex='\d+',message='數字啦幹')
				])
	oil = StringField(
			'加了多少公升 ?',
			validators=[
				DataRequired(),
				Regexp(regex='\d+',message='數字啦幹')
			])
	submit = SubmitField('幫我算算')

# 漂亮的考試系統 / BeautifulExamForm
class BeautifulExamForm(FlaskForm):
	usernamef = StringField(
				'請輸入學號',
				validators=[
					DataRequired(),
				])
	passwordf = PasswordField(
				'請輸入密碼',
				validators=[
					DataRequired(),
				])
	submit = SubmitField('取得考試時間')

class AutoExamForm(FlaskForm):
	submit = SubmitField('提交')

class UpperForm(FlaskForm):
	textin = StringField('請輸入要轉換的句子',
				validators=[DataRequired()
				])
	submit = SubmitField('轉換')








