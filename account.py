from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=15)])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('signup')
class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=15)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')