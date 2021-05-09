from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField, RadioField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from spaceconnect.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class ApplyForm(FlaskForm):
    fullname = StringField('Fullname', validators=[DataRequired(), Length(min=5,max=30)])
    age = IntegerField('Age', validators=[DataRequired()])
    mission = StringField('Which mission would you prefer(Mission 1 or 2)', validators= [DataRequired()])
    content = TextAreaField('Describe your abilities', validators=[DataRequired(), Length(max=100)])
    apply = SubmitField('Apply')