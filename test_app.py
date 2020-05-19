import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, User, Blog_Post

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
           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOTYwZmQxZGZhYmFlMGM4OTRhODY1MCIsImF1ZCI6ImJsb2dvc3BoZWFyIiwiaWF0IjoxNTg5ODQ2NTIyLCJleHAiOjE1ODk4NTM3MjIsImF6cCI6Ik1qRUdSbGhVRGtQYlFRVUI2V2MzOXdpMGlCMHE0bFVaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YmxvZ19wb3N0cyIsImdldDp1c2VycyIsInBhdGNoOmJsb2dfcG9zdHMiLCJwb3N0OmJsb2dfcG9zdHMiLCJwb3N0OnVzZXJzIl19.K-aMUsIz57jxNDpnapX4jAcDjy-EuiDc8DwIMEKFLtwcmzy3n41CIfV-RMuHXkKhA3YJnamrZHW81sHzr7CpY7-FElJBrKSOZmI80pk5p9Ldcmor98I2gKIwApBg3RopEMFTw445tD-7V368_hl7MsqCSbSjpmfFNT_az4FYruPpGSTvNm4K8JycjnWopBgJABPJBLOMmiM7hLQ0kxm9D33DHiM3e4i09Ile4i4fH1dlymku8zkibH7obbrozPufitjPRSrGuAJaOD12ekR-XcVZE_ORu0Um_457Cs0isB7GU-O0dhg2-rhtQFkQkoLZ3lOrWMJUW5J0k2vX5VXHVw'
        }

        self.blogger_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwMjg0MTU3NzQyNjA0NzMyMzQ4IiwiYXVkIjpbImJsb2dvc3BoZWFyIiwiaHR0cHM6Ly9kZXYtZnVsbHN0YWNrLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODk4NDk2NDksImV4cCI6MTU4OTg1Njg0OSwiYXpwIjoiTWpFR1JsaFVEa1BiUVFVQjZXYzM5d2kwaUIwcTRsVVoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6YmxvZ19wb3N0cyIsInBvc3Q6YmxvZ19wb3N0cyJdfQ.RVdY_tcG8w8rUj7_vD2cCC1BFm_Yg_HSMiB7FBwOXM2YbfuwdtpaEIPFxNF1RYgbbvJvP4Ox-YytHfMGbp-OiI4J3k2DC-PvMzSiLkKuyRF-2Nu3XssO3evrbHHvufSi1hTvmUAY2Lg1W7x03yB7DM7ySr5OD4DrnUDW7hHYWCdxwxI8NzsZzJo1i8HOFk_6_SU2aFV9u8wo4VwwNWIMXuKiJ6YXgJNQwVpiJNNfcsOG6aA40y-SM5Znwl9f5H5SMEj8N2qqnKSqTkB34gHwlG7OHyxymMnPo05L7vmKweTXDNnJWEe2Cc7gS2eNVGyNHY-MyzFT5T3H9rIBcWYybQ'
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

    def test_POST_blog_post(self):
        res = self.client().post('/blog_posts', json=self.new_blog, headers=self.admin_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])

    def test_POST_blog_posts_fail(self):
        basic_auth_fail(self, '/blog_posts', self.client().post)

    def test_GET_blog_posts(self):
        data = check_basic_success(self, '/blog_posts', self.client().get)
        print(data)

    def test_GET_specific_post(self):
        check_basic_success(self, '/blog_posts/2', self.client().get)

    def test_GET_specific_post_fail(self):
        check_basic_failure(self, '/blog_posts/100000', 404, self.client().get)

    def test_GET_blogs_for_user(self):
        data = check_basic_success(self, '/users/1/blog_posts', self.client().get, self.admin_header)
        self.assertEqual(1, data['user'])
    
    def test_GET_blogs_for_user_fail(self):
        basic_auth_fail(self, '/users/1/blog_posts', self.client().get)

    def test_DELETE_blog_post_fail(self):
        basic_auth_fail(self, '/blog_posts/1', self.client().delete, headers=self.blogger_header)

    def test_DELETE_blog_post(self):
        # If testing this multiple times, change the id it deletes.
        check_basic_success(self, '/blog_posts/1', self.client().delete, headers=self.admin_header)

    def test_PATCH_blog_post(self):
        # check_basic_success(self, '/blog_posts/42', self.client().patch, headers=self.admin_header)
        title = "this is my title"
        res = self.client().patch('/blog_posts/42', json={'title': title}, headers=self.blogger_header)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEquals(data['blog_post'].get('title'), title)

    def test_PATCH_blog_post_fail(self):
        basic_auth_fail(self, '/blog_posts/42', self.client().patch)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()