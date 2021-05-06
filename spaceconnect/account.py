from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from spaceconnect.model import User
class Registration(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=3,max=20)])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=15)])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('signup')
    def validate_user(self,username):
        user =  User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken')
    def validate_email(self,email):
        email =  User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is taken')

class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8,max=15)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')