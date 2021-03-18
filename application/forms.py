from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField
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

class EditWorkerForm(FlaskForm):
    Id = IntegerField(label='ID:', validators=[DataRequired()])
    FirstName = StringField(label='First Name: ', validators=[DataRequired()])
    LastName = StringField(label='Last Name: ', validators=[DataRequired()])
    Age = IntegerField(label='Age: ', validators=[DataRequired()])
    PhoneNumber = StringField(label='Phone Number: ', validators=[DataRequired()])
    PhoneNumber2 = StringField(label='2nd Phone Number (Optional): ')
    Email = StringField(label='Email Address: ', validators=[DataRequired()])
    Email2 = StringField(label='2nd Email Address (Optional): ')
    Workers_id = IntegerField(label='Workers Contact Details ID:', validators=[DataRequired()])
    Mowing = BooleanField(label='Mowing: ')
    Hedging = BooleanField(label='Hedging: ')
    Fencing = BooleanField(label='Fencing: ')
    Patios = BooleanField(label='Patios: ')
    BrickLaying = BooleanField(label='Brick Laying: ')
    Workers_id = IntegerField(label='Workers Capability ID:', validators=[DataRequired()])
    Submit = SubmitField(label='Update')