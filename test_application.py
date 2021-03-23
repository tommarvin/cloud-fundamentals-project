import unittest

from flask_testing import TestCase
from application import db, app
from application.models import *
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        """
        will be called before every test
        """
        db.create_all()

        worker=Workers(firstname='Test', lastname='One', age=1)
        db.session.add(worker)
        db.session.commit()
        workercd=ConD1(phone1='1', phone2='2', email1='e1', email2='e2', workers_id=worker.id)
        workercb=Capab(mowing=True, hedging=True, fencing=False, patios=False, bricklaying=True, workers_id=worker.id)
        db.session.add(workercd)
        db.session.add(workercb)
        db.session.commit()

        job=Jobs(start='test', numbworkers=1)
        db.session.add(job)
        db.session.commit()
        jobad=Address(address1='1', address2='2', address3='3', postcode='4', jobs_id=job.id)
        jobrq=Req(mowing=True, bricklaying=False, fencing=True, hedging=False,patios=False,jobs_id=job.id)
        jobcd=CstmDt(customername='test', customeremail='1', customerphone='1', jobs_id=job.id)
        db.session.add(jobad)
        db.session.add(jobrq)
        db.session.add(jobcd)
        db.session.commit()

        team=Team(teamnumber=1, jobs_id=job.id, workers_id=worker.id)
        db.session.add(team)
        db.session.commit()






    def tearDown(self):
        """
        will be called after every test
        """
        db.session.remove()
        db.session.commit()


class TestDB(TestBase):


    def test_workers_model(self):
        """
        Test that the sql database is connected to my application
        """
        self.assertEqual(Workers.query.count(), 1)






class TestViews(TestBase):
    def test_index_get(self):
        """
        Test index
        """
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_addworker_get(self):
        """
        Test Add workers
        """
        response = self.client.get(url_for('addworker'))
        self.assertEqual(response.status_code, 200)

    def test_viewworkers_get(self):
        """
        Test view workers
        """
        response = self.client.get(url_for('viewworkers'))
        self.assertEqual(response.status_code, 200)


    def test_editworker_get(self):
        """
        Test edit workers selection
        """
        worker=Workers.query.first()
        id = worker.id
        response = self.client.get(url_for('editworker', id=id))
        self.assertEqual(response.status_code, 200)

    def test_edit_get(self):
        """
        Test editing of the worker
        """
        worker=Workers.query.first()
        id = worker.id
        response = self.client.get(url_for('edit', id=id))
        self.assertEqual(response.status_code, 302)

    def test_remove_get(self):
        """
        Test remove selection workers
        """
        worker=Workers.query.first()
        id = worker.id
        response = self.client.get(url_for('remove', id=id))
        self.assertEqual(response.status_code, 302)


    def test_view_CD_get(self):
        """
        Test viewing the added workers contact details
        """
        worker=Workers.query.first()
        id = worker.id
        response = self.client.get(url_for('View_CD', id=id))
        self.assertEqual(response.status_code, 200)

    def test_viewjobs_get(self):
        """
        Test viewing the jobs
        """
        response = self.client.get(url_for('viewjobs'))
        self.assertEqual(response.status_code, 200)


    def test_View_Custm_CD_get(self):
        """
        Test viewing the customer details 
        """
        jobcd = Jobs.query.first()
        id = jobcd.id
        response = self.client.get(url_for('View_Custm_CD', id=id))
        self.assertEqual(response.status_code, 200)

    def test_View_Address_get(self):
        """
        Test viewing the jobs address
        """
        jobcd = Jobs.query.first()
        id = jobcd.id
        response = self.client.get(url_for('View_Address', id=id))
        self.assertEqual(response.status_code, 200)

    def test_Create_Team_get(self):
        """
        Test Creating a team for a job
        """
        job=Jobs.query.first()
        id = job.id
        response = self.client.get(url_for('Create_Team', id=id))
        self.assertEqual(response.status_code, 200)

    def test_Add_First_Member_get(self):
        """
        Test Adding first member to the team
        """
        job=Jobs.query.first()
        id = job.id
        worker=Workers.query.first()
        ID=worker.id
        response = self.client.post(url_for('Add_First_Member', id=id, ID=ID))
        self.assertEqual(response.status_code, 200)

    def test_Add_Job_get(self):
        """
        Test Adding a new job
        """
        response = self.client.get(url_for('Add_Job'))
        self.assertEqual(response.status_code, 200)


    def test_removeMember_get(self):
        """
        Test removing team member
        """
        job=Jobs.query.first()
        id = job.id
        worker=Workers.query.first()
        ID=worker.id
        response = self.client.get(url_for('removeMember', id=id, worker_id=ID))
        self.assertEqual(response.status_code, 200)

    def test_editjob_get(self):
        """
        Test selecting job to edit
        """
        jobcd = Jobs.query.first()
        id = jobcd.id
        response = self.client.get(url_for('editjob', id=id))
        self.assertEqual(response.status_code, 200)

    def test_editj_get(self):
        """
        Test editing job 
        """
        jobcd = Jobs.query.first()
        id = jobcd.id
        response = self.client.get(url_for('editj', id=id))
        self.assertEqual(response.status_code, 302)

    def test_removejob_get(self):
        """
        Test selecting and removing job
        """
        jobcd = Jobs.query.first()
        id = jobcd.id
        response = self.client.get(url_for('removejob', id=id))
        self.assertEqual(response.status_code, 302)








