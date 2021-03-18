from application import db


class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    contact_details = db.relationship('ConD1', backref=('workers'))
    capabilities = db.relationship('Capab', backref=('workers'))
    
        
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


# class Jobs(db.Model):
#     id = db.Column(db.Integer, Primary_Key=True)
#     Address = db.relationship('Address', backref='jobs')

# class Address(db.Model):
#     id = db.Column(db.Integer, Primary_Key=True)
#     house = db.Column(db.String(25), nullable=False)
#     roadname = db.Column(db.String(25), nullable=False)
#     town = db.Column(db.String(25), nullable=False)
#     postcode = db.Column(db.String(8), nullable=False)
#     jobs_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))