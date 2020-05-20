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
           'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOTYwZmQxZGZhYmFlMGM4OTRhODY1MCIsImF1ZCI6ImJsb2dvc3BoZWFyIiwiaWF0IjoxNTg5OTE3ODU1LCJleHAiOjE1ODk5ODk4NTUsImF6cCI6Ik1qRUdSbGhVRGtQYlFRVUI2V2MzOXdpMGlCMHE0bFVaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YmxvZ19wb3N0cyIsImdldDp1c2VycyIsInBhdGNoOmJsb2dfcG9zdHMiLCJwb3N0OmJsb2dfcG9zdHMiLCJwb3N0OnVzZXJzIl19.mExeavcdHsp6qrKxWYm6nQ-h-fqZARgGpQpFM6IxAnX1WZRl9pjH0jr6pqUh4-EQm1Uw9_0_wcd_skeA_HgHTwZbRHde8DjvBRHcg0XbXpsq9Jaey8Zj5ozSfk8ferAo3V30M7hXRd0xJSCOUXJbLG96Gf9mOHxeT52A6XmAZtuD1febBiZilMOjUYiZIH5lNFZiywRfOs2PiZaMAEaw2KAEOa0lJnVsy744BM21x31097mKuvk2uCmy-lZPDQ25yJ60szb6o4lKxA_-clcJJmSGsBs42tLXRRB4MRL4DbEES74utavY_g9-YJMHd6vjjZInyt8ABfJGSkc54RmZpQ'
        }

        self.blogger_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwMjg0MTU3NzQyNjA0NzMyMzQ4IiwiYXVkIjpbImJsb2dvc3BoZWFyIiwiaHR0cHM6Ly9kZXYtZnVsbHN0YWNrLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODk5MTc5MzgsImV4cCI6MTU4OTk4OTkzOCwiYXpwIjoiTWpFR1JsaFVEa1BiUVFVQjZXYzM5d2kwaUIwcTRsVVoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6YmxvZ19wb3N0cyIsInBvc3Q6YmxvZ19wb3N0cyJdfQ.lUsjl8L0GhmrX4-JMN-KUd1eIi-X8WJix5MO4d_oK3GRCpx9rlbpoaJGPyF78V25nIZQWipd_HQJUT5hx0W_YkQuc8xfUbGEYPa3csMV88w2vu1tVWMd9h2uEmIGlX8rZkWznyEeD0SaRuR89kzXfN3YcsbxSL3vxYBhysRc4wIXyI4Erw344razV3qR-fJlE7Osq0oVW4eNZ9bsn5BCsoLjO_Kb-kr3qHP2aS-wfMNBdKapdijYugj1vrjF6EIIxduRkmxvI3IefZOJl7bOUu-tQmdO9uWzRn3bBzqKqu44AVfuZEWIpKZ9gsLXzGPl36lO67Gz3pGkuYDAZ-HyAg'
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