from application import db
from flask_sqlalchemy import SQLAlchemy, BaseQuery

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamnumber = db.Column(db.Integer, nullable=False)
    workers_id = db.Column(db.Integer, db.ForeignKey('workers.id'))
    jobs_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=True)


class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    contact_details = db.relationship('ConD1', backref=('workers'))
    capabilities = db.relationship('Capab', backref=('workers'))
    team = db.relationship('Team', backref='workers')


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(20), nullable=False)
    numbworkers = db.Column(db.Integer, nullable=False)
    address = db.relationship('Address', backref='job')
    req = db.relationship('Req', backref='jobs')
    cstmdt = db.relationship('CstmDt', backref='jobs')
    team = db.relationship('Team', backref='jobs')


class ConD1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone1 = db.Column(db.String(20), nullable=False)
    phone2 = db.Column(db.String(20))
    email1 = db.Column(db.String(50), nullable=False)
    email2 = db.Column(db.String(50))
    workers_id = db.Column(db.Integer, db.ForeignKey('workers.id'), nullable=False)
   

class Capab(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mowing = db.Column(db.Boolean())
    hedging = db.Column(db.Boolean())
    fencing = db.Column(db.Boolean())
    patios = db.Column(db.Boolean())
    bricklaying = db.Column(db.Boolean())
    workers_id = db.Column(db.Integer, db.ForeignKey('workers.id'), nullable=False)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(25), nullable=False)
    address2 = db.Column(db.String(25), nullable=False)
    address3 = db.Column(db.String(25), nullable=False)
    postcode = db.Column(db.String(8), nullable=False)
    jobs_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)


class Req(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mowing = db.Column(db.Boolean())
    hedging = db.Column(db.Boolean())
    fencing = db.Column(db.Boolean())
    patios = db.Column(db.Boolean())
    bricklaying = db.Column(db.Boolean())
    jobs_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)


class CstmDt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(50), nullable=False)
    customerphone = db.Column(db.String(20), nullable=False)
    customeremail = db.Column(db.String(50), nullable=False)
    jobs_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)


