import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, User, Blog

def check_basic_success(self, url, http_method, headers=None):
    return basic_check(self, url, http_method, self.assertTrue, headers=headers)

def check_basic_failure(self, url, code, http_method, headers=None):
    return basic_check(self, url, http_method, self.assertFalse, code, headers=headers)

def basic_check(self, url, http_method, assert_method, code=200, headers=None):
    res = http_method(url, headers=headers)
    data = json.loads(res.data)
    assert_method(data['success'])
    self.assertEqual(res.status_code, code)
    return data

def basic_auth_fail(self, url, http_method, headers=None):
    res = http_method(url, headers=headers)
    data = json.loads(res.data)
    self.assertTrue(res.status_code == 401)

class BlogOSphearTestCase(unittest.TestCase):
    """This class represents the BlogOSphear test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "reasons_for_hope_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', 'Blue84paired.', 'localhost:5432', self.database_name)
        self.headers = {}
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_blog = {
            'title': 'title',
            'body': 'this is my body',
            'author_id': 1
        }

        self.new_user = {
            'name': 'JayMeck',
            'email': 'Totally@real.com',
        }

        self.admin_header = {
           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOTYwZmQxZGZhYmFlMGM4OTRhODY1MCIsImF1ZCI6ImJsb2dvc3BoZWFyIiwiaWF0IjoxNTg5OTc5MzEyLCJleHAiOjE1OTAwNTEzMTIsImF6cCI6Ik1qRUdSbGhVRGtQYlFRVUI2V2MzOXdpMGlCMHE0bFVaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YmxvZ3MiLCJnZXQ6dXNlcnMiLCJwYXRjaDpibG9ncyIsInBvc3Q6YmxvZ3MiLCJwb3N0OnVzZXJzIl19.YJy0P9YBQs4sTMRjHFaOYuNZYGcz3EwHnhGqVf7y3-U3rCuLlOwQJHOi8R6WMp4N0gnnQuFFG0QaTK6QTn5ef4oBvr3MRZOI40h8i8yYGEGDS3jF0XZDQ9rqTUIBaIHm4AqjoNTE3x_PWO0A424H2e-cqMP5HRpg-wKIflt9LBAL8zFE7VkEcDWsL09Z14cgNTLthoS_J6nHq7fTacKfs2HSySP16oIwkLOuE71MTk-4Je_6-7TCEdC6HIEOieJKA5yLfAntvxEfG3AFOw1GLikhEXGy84tNYhNk2wwssy0At5-KiDeo0JXqBpejG-02TF8CYwLIRDwjcRMhs5SsJA'
        }

        self.blogger_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOGUyNzkzMWFmOTcxMGM3Mjc5MjcwNyIsImF1ZCI6ImJsb2dvc3BoZWFyIiwiaWF0IjoxNTg5OTc4OTY5LCJleHAiOjE1OTAwNTA5NjksImF6cCI6Ik1qRUdSbGhVRGtQYlFRVUI2V2MzOXdpMGlCMHE0bFVaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDpibG9ncyIsInBvc3Q6YmxvZ3MiXX0.EWn0ft8NiisR5klTxkJzJ7CwW_x3yVpQiT0-51HQPmz2ODRak7SMSgDQKfpYMZMlSHOEt0CMRi0vCe8uLn4tDuCzBEmQEzazXi4PTVOeuPAicmEdY9LBZPr3bPkWR8o4qDLrgc14_dh4xhS14nm-GpCqcHHG383ycCF3ysqXfvmAQEOXKpK-2dh78QZTd11-nBF7HigzNncDv4qYL0T9pZ56aZ6HpNIuxq-6BP849bgoWmxXZ-XClXnXLHalKZqB9yg6ufKGHf76DeMrLRPYya4mZlMrvr5KLidIJetgKUqw5UPT3i4GdsKFeq81GNEiuj1QqZrfVOdbPa34LDP5Qg'
        }
    
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_GET_users(self):
        data = check_basic_success(self, '/users',self.client().get, self.admin_header)
    
    def test_GET_users_fail(self):
        basic_auth_fail(self, '/users', self.client().get)

    def test_POST_users(self):
        res = self.client().post('/users', json=self.new_user, headers=self.admin_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_POST_users_fail(self):
        basic_auth_fail(self, '/users', self.client().post, headers=self.blogger_header)

    def test_POST_blogs(self):
        res = self.client().post('/blogs', json=self.new_blog, headers=self.admin_header)
        data = json.loads(res.data)
        print(data)
        self.assertTrue(data['success'])

    def test_POST_blogs_fail(self):
        basic_auth_fail(self, '/blogs', self.client().post)

    def test_GET_blogs(self):
        data = check_basic_success(self, '/blogs', self.client().get)
        print(data)

    def test_GET_specific_post(self):
        check_basic_success(self, '/blogs/1', self.client().get)

    def test_GET_specific_post_fail(self):
        check_basic_failure(self, '/blogs/100000', 404, self.client().get)

    def test_GET_blogs_for_user(self):
        data = check_basic_success(self, '/users/1/blogs', self.client().get, self.admin_header)
        self.assertEqual(1, data['user'])
    
    def test_GET_blogs_for_user_fail(self):
        basic_auth_fail(self, '/users/1/blogs', self.client().get)

    def test_PATCH_blogs(self):
        title = "this is my title"
        res = self.client().patch('/blogs/1', json={'title': title}, headers=self.blogger_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEquals(data['blog'].get('title'), title)

    def test_PATCH_blogs_fail(self):
        basic_auth_fail(self, '/blogs/42', self.client().patch)

    def test_DELETE_blogs_fail(self):
        basic_auth_fail(self, '/blogs/1', self.client().delete, headers=self.blogger_header)

    def test_DELETE_blogs(self):
        # If testing this multiple times, change the id it deletes.
        check_basic_success(self, '/blogs/1', self.client().delete, headers=self.admin_header)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()