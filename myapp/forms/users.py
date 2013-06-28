from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField, RadioField
from flask.ext.wtf import Required, Length, validators

from google.appengine.ext import ndb
from myapp.models.users import User

def unique_email(form, field):
    if User.gql ('WHERE email = :1', field.data).count() > 0:
        raise validators.ValidationError('That email is already in use, please select another.')

class LoginForm(Form):
    email = TextField('Email', [validators.Length(min=4, max=225)])
    password = TextField('Password')

class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=225)])
    email = TextField('Email', validators = [validators.Required(), validators.length(max=200),  
unique_email])
