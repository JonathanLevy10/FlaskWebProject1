#Imports
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import Form, BooleanField, PasswordField
from wtforms import TextField, TextAreaField, SelectField
from wtforms import validators, ValidationError
from wtforms.fields.html5 import DateField

from wtforms.validators import DataRequired, Email, Length
from wtforms.validators import InputRequired



#classes for expand and collapse
class ExpandForm(FlaskForm):
    submit1 = SubmitField('Expand')
    name="Expand" 
    value="Expand"

class CollapseForm(FlaskForm):
    submit2 = SubmitField('Collapse')
    name="Collapse" 
    value="Collapse"



    #class for register also makes sure that all data is submited by user.
class RegisterFormStructure(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired])
    lastname = StringField('Last Name', validators = [DataRequired])
    phonenumber = StringField('Phone Number')
    emailaddress = StringField('E-Mail Address', validators = [DataRequired, Email])
    username = StringField('Username', validators = [DataRequired])
    password = PasswordField('Password', validators = [DataRequired, Length(8)])
    submit = SubmitField('Register')
    #class for log in also makes sure that all data is submited by user.
class LoginFormStructure(FlaskForm):
    username = StringField('Username', validators = [DataRequired])
    password = PasswordField('Password', validators = [DataRequired])
    submit = SubmitField('Login')

    #class that submites choice of category for query
class QueryForm(FlaskForm):
    category = SelectField('Category', validators = [DataRequired])
    submit = SubmitField('Query')
