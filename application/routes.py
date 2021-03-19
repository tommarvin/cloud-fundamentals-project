from application import app
from flask import render_template, request, redirect
from application.models import Capab, Workers, ConD1, Jobs, Address, Req, CstmDt
from application import db
from application.forms import AddJobForm, WorkerForm





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






@app.route('/My-Jobs', methods=['GET', 'POST'])
def viewjobs():
    b = []
    for worker in Workers.query.all():
        b.append(worker)
    x = (len(b)+50)
    
    return render_template('myjobs.html', Jobs=Jobs, Req=Req, Address=Address, CstmDt=CstmDt, x=x)


@app.route('/My-Jobs/View-Customer-ContactDetails/<id>', methods=['GET', 'POST'])
def View_Custm_CD(id):
    return render_template('viewcustomer.html', id=id, CstmDt=CstmDt)

@app.route('/My-Jobs/View-Address/<id>', methods=['GET', 'POST'])
def View_Address(id):
    return render_template('viewaddress.html', id=id, Address=Address)


@app.route('/Add-Jobs', methods=['POST', 'GET'])
def Add_Job():
    form = AddJobForm()

    if request.method  == 'POST':
        start=form.StartDate.data
        numbworkers=form.WorkersReq.data

        mowing=form.Mowing.data
        hedging=form.Hedging.data
        fencing=form.Fencing.data
        patios=form.Patios.data
        bricklaying=form.BrickLaying.data

        address1=form.Address1.data
        address2=form.Address2.data
        address3=form.Address3.data 
        postcode=form.Postcode.data

        customername=form.CustomerName.data
        customerphone=form.CustomerPhone.data
        customeremail=form.CustomerEmail.data

        if form.validate_on_submit:
            job1 = Jobs(start=start, numbworkers=numbworkers)
            db.session.add(job1)
            db.session.commit()
            job2 = Req(mowing=mowing, hedging=hedging, fencing=fencing, patios=patios, bricklaying=bricklaying, jobs_id=job1.id)
            db.session.add(job2)
            job3 = Address(address1=address1, address2=address2, address3=address3, postcode=postcode, jobs_id=job1.id)
            db.session.add(job3)
            job4 = CstmDt(customername=customername, customerphone=customerphone, customeremail=customeremail, jobs_id=job1.id)
            db.session.add(job4) 
            db.session.commit()
            return redirect('/My-Jobs')
    return render_template('addjob.html', form=form)