from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase


testapp = Flask(__name__)
testapp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://project-db:root@34.89.124.0/testdb'
db = SQLAlchemy(testapp)
testapp.config['SECRET_KEY'] = 'TEM_test_SK123'







if __name__ == '__main__':
    testapp.run(debug=True)

from application.models import Workers, ConD1, Capab