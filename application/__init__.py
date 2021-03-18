from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
import gunicorn
from wtforms import StringField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://project-db:root@34.89.124.0/wgc'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'TEM_SK123'





from application import routes