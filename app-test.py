# from flask import Flask, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_testing import TestCase
# from werkzeug.wrappers import Response
# from run import app, db
# from application.models import Workers, ConD1, Capab, Jobs, Req, Address, CstmDt, Team



# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
#         SECRET_KEY='TEST_SECRET_KEY',
#         DEBUG=True,
#         WTF_CSRF_ENABLED=False)
#         return app

#     def setUp(self):
#         db.create_all()


#     def tearDown(self):
#         db.session.remove()
#         db.session.commit()


# class TestViews(TestBase):
#     def test_index_get(self):
#         response = self.client.get(url_for('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(response.data)