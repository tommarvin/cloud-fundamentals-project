from application import app
from flask import render_template, request, redirect
from application.models import Capab, Workers, ConD1
from application import db
from application.forms import WorkerForm





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Add-Workers', methods = ['GET', 'POST'])
def addworker():
    form = WorkerForm()

    if request.method=='POST':
        FirstName = form.FirstName.data
        LastName = form.LastName.data
        Age = form.Age.data
        PhoneNumber = form.PhoneNumber.data
        PhoneNumber2 = form.PhoneNumber2.data
        Email = form.Email.data
        Email2 = form.Email2.data
        Mowing = form.Mowing.data
        Hedging = form.Hedging.data
        Fencing = form.Fencing.data
        Patios = form.Patios.data
        BrickLaying = form.BrickLaying.data

        if form.validate_on_submit:
            Worker1 = Workers(firstname=FirstName, lastname=LastName, age=Age)
            db.session.add(Worker1)
            db.session.commit()
            Worker1_Cd = ConD1(phone1=PhoneNumber, phone2=PhoneNumber2, email1=Email, email2=Email2, workers_id=Worker1.id)
            Worker1_Cb = Capab(mowing=Mowing, hedging=Hedging, fencing=Fencing, patios=Patios, bricklaying=BrickLaying, workers_id=Worker1.id)
            db.session.add(Worker1_Cb)
            db.session.add(Worker1_Cd)
            db.session.commit()
            return redirect('/My-Workers')
    return render_template('addworkers.html', title='addworker', form=form)



@app.route('/My-Workers', methods=['GET', 'POST'])
def viewworkers():
    a = []
    for worker in Workers.query.all():
        a.append(worker)
    y = (len(a)+50)
    
    return render_template('myworkerscopy.html', Workers=Workers, ConD1=ConD1, Capab=Capab, y=y)




@app.route('/Edit/<id>', methods=['GET', 'POST'])
def editworker(id):
    return render_template('edit.html', id=id, Workers=Workers, Capab=Capab, ConD1=ConD1)



@app.route('/My-Workers/Edit/<id>', methods=['GET', 'POST'])
def edit(id):

    if request.method == 'POST':
        workerD = Workers.query.filter_by(id=id).first()    
        workercd = ConD1.query.filter_by(workers_id=id).first()
        workercb = Capab.query.filter_by(workers_id=id).first()
        
        workerD.firstname = request.form.get('firstname')
        workerD.lastname = request.form.get('lastname')
        workerD.age = request.form.get('age')

        workercd.phone1 = request.form.get('phone1')
        workercd.phone2 = request.form.get('phone2')
        workercd.email1 = request.form.get('email1')
        workercd.email2 = request.form.get('email2')
        
        workercb.mowing = bool(request.form.get('mowing'))
        workercb.hedging = bool(request.form.get('hedging'))
        workercb.fencing = bool(request.form.get('fencing'))
        workercb.patios = bool(request.form.get('patios'))
        workercb.bricklaying = bool(request.form.get('bricklaying'))

        db.session.commit()
    
    return redirect('/My-Workers')


@app.route('/My-Workers/Remove/<id>', methods=['GET', 'POST'])
def remove(id):
    delete1 = Workers.query.filter_by(id=id).first()
    delete2 = ConD1.query.filter_by(workers_id=id).first()
    delete3 = Capab.query.filter_by(workers_id=id).first()
    db.session.delete(delete1)
    db.session.delete(delete2)
    db.session.delete(delete3)
    db.session.commit()
    return redirect('/My-Workers')




@app.route('/My-Workers/View-ContactDetails/<id>', methods=['GET', 'POST'])
def View_CD(id):
    return render_template('view-contact-details.html', id=id, Workers=Workers, ConD1=ConD1)