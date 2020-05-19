import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

try:
    database_path = os.environ['DATABASE_URL']
except:
    database_path = "postgres://postgres:Blue84paired.@localhost:5432/reasons_for_hope"

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

"""
    This is the base model which handles inserting, 
    updating, and deleting. These methods will be available for 
    each class which inherits this basic model.  
"""
class Basic_Model():
    def insert(self):
        db.session.add(self)
        db.session.commit()
  
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

"""
    This is the blog post class. Each blog contains 
    a title, body, and author. 
"""
class Blog_Post(Basic_Model, db.Model):
    __tablename__ = 'blog_post'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, body, author_id):
        self.author_id = author_id
        self.body = body
        self.title = title 
    
    def format(self):
        return {
            'id' : self.id,
            'title': self.title,
            'body': self.body,
            'author_id': self.author_id,
        }
'''
User
Has Name, email, blog posts, and Id
'''

class User(Basic_Model, db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email= Column(String, nullable=False)
    blog_posts = db.relationship('Blog_Post', backref='user', lazy=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email':self.email,
            'blog_posts': [blog.format() for blog in self.blog_posts]
        }

