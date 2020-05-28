from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange, Regexp


class LoginForm(FlaskForm):
	email = StringField("Email address")
	password = StringField("Password")
	submit = SubmitField('LET ME IN')