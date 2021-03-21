from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, DateField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired
from . import app 



app.config['SECRET_KEY'] = 'TEM_SK123'


class WorkerForm(FlaskForm):
    FirstName = StringField(label='First Name: ', validators=[DataRequired()])
    LastName = StringField(label='Last Name: ', validators=[DataRequired()])
    Age = IntegerField(label='Age: ', validators=[DataRequired()])
    PhoneNumber = StringField(label='Phone Number: ', validators=[DataRequired()])
    PhoneNumber2 = StringField(label='2nd Phone Number (Optional): ')
    Email = StringField(label='Email Address: ', validators=[DataRequired()])
    Email2 = StringField(label='2nd Email Address (Optional): ')
    Mowing = BooleanField(label='Mowing: ')
    Hedging = BooleanField(label='Hedging: ')
    Fencing = BooleanField(label='Fencing: ')
    Patios = BooleanField(label='Patios: ')
    BrickLaying = BooleanField(label='Brick Laying: ')
    Submit = SubmitField(label='Add Worker')

class AddJobForm(FlaskForm):
    Address1 = StringField(label='Address Line 1: ', validators=[DataRequired()])
    Address2 = StringField(label='Address Line 2: ', validators=[DataRequired()])
    Address3 = StringField(label='Address Line 3: ', validators=[DataRequired()])
    Postcode = StringField(label='Postcode: ', validators=[DataRequired()])
    StartDate = StringField(label='Start Date: ', validators=[ DataRequired()])
    Mowing = BooleanField(label='Mowing: ')
    Hedging = BooleanField(label='Hedging: ')
    Fencing = BooleanField(label='Fencing: ')
    Patios = BooleanField(label='Patios: ')
    BrickLaying = BooleanField(label='Brick Laying: ')
    WorkersReq = IntegerField(label='Estimated Number of Workers required: ', validators=[DataRequired()])
    CustomerName = StringField(label='Customers Full Name: ', validators=[DataRequired()])
    CustomerPhone = StringField(label='Customers Phone Number: ', validators=[DataRequired()])
    CustomerEmail = StringField(label='Customers Email Address: ', validators=[DataRequired()])
    Submit = SubmitField(label='Add Job')