from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from wtforms.validators import Email, EqualTo, ValidationError
from app.auth.models.user_model import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), ])
    password = PasswordField('Password', [DataRequired()])
    re_password = PasswordField('Re-enter Password',
                                [DataRequired(), EqualTo(fieldname='password', message='Enter same password')])
    email = EmailField('Email', validators=[Email()])
    submit = SubmitField('Sign Up')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken')


class ResendForm(FlaskForm):
    email = EmailField('Your Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Resend email')
