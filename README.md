# PersonalWebsite-Backend
The backend of my website.

It is hosted at: https://reasons-for-hope.herokuapp.com/

JWT token for Blogger Role: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwMjg0MTU3NzQyNjA0NzMyMzQ4IiwiYXVkIjpbImJsb2dvc3BoZWFyIiwiaHR0cHM6Ly9kZXYtZnVsbHN0YWNrLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1ODk5MTc5MzgsImV4cCI6MTU4OTk4OTkzOCwiYXpwIjoiTWpFR1JsaFVEa1BiUVFVQjZXYzM5d2kwaUIwcTRsVVoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsicGF0Y2g6YmxvZ19wb3N0cyIsInBvc3Q6YmxvZ19wb3N0cyJdfQ.lUsjl8L0GhmrX4-JMN-KUd1eIi-X8WJix5MO4d_oK3GRCpx9rlbpoaJGPyF78V25nIZQWipd_HQJUT5hx0W_YkQuc8xfUbGEYPa3csMV88w2vu1tVWMd9h2uEmIGlX8rZkWznyEeD0SaRuR89kzXfN3YcsbxSL3vxYBhysRc4wIXyI4Erw344razV3qR-fJlE7Osq0oVW4eNZ9bsn5BCsoLjO_Kb-kr3qHP2aS-wfMNBdKapdijYugj1vrjF6EIIxduRkmxvI3IefZOJl7bOUu-tQmdO9uWzRn3bBzqKqu44AVfuZEWIpKZ9gsLXzGPl36lO67Gz3pGkuYDAZ-HyAg

JWT token for Admin Role: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd5T0R4NGZWQ1FaWHlLYVlseFZqaCJ9.eyJpc3MiOiJodHRwczovL2Rldi1mdWxsc3RhY2suYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlOTYwZmQxZGZhYmFlMGM4OTRhODY1MCIsImF1ZCI6ImJsb2dvc3BoZWFyIiwiaWF0IjoxNTg5OTE3ODU1LCJleHAiOjE1ODk5ODk4NTUsImF6cCI6Ik1qRUdSbGhVRGtQYlFRVUI2V2MzOXdpMGlCMHE0bFVaIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YmxvZ19wb3N0cyIsImdldDp1c2VycyIsInBhdGNoOmJsb2dfcG9zdHMiLCJwb3N0OmJsb2dfcG9zdHMiLCJwb3N0OnVzZXJzIl19.mExeavcdHsp6qrKxWYm6nQ-h-fqZARgGpQpFM6IxAnX1WZRl9pjH0jr6pqUh4-EQm1Uw9_0_wcd_skeA_HgHTwZbRHde8DjvBRHcg0XbXpsq9Jaey8Zj5ozSfk8ferAo3V30M7hXRd0xJSCOUXJbLG96Gf9mOHxeT52A6XmAZtuD1febBiZilMOjUYiZIH5lNFZiywRfOs2PiZaMAEaw2KAEOa0lJnVsy744BM21x31097mKuvk2uCmy-lZPDQ25yJ60szb6o4lKxA_-clcJJmSGsBs42tLXRRB4MRL4DbEES74utavY_g9-YJMHd6vjjZInyt8ABfJGSkc54RmZpQ 

## Motivation 
This project was started because of the Udacity Full Stack Nano degree program. However, I build this because I wanted to make an API which could be used as a simple way to make a blog. I am currently working on a VueJS front end to pair with this backend. 

## Style Guide
The code adhears to the Pep8 style guide

## Requirements Setup
In order to run this locally, run
python3 -m venv env
source env/Scripts/activate
pip install -r requirements.txt

This will install all the needed dependancies from the requirements
file. 

## Database setup. 
Login to psql and create a database called:reasons_for_hope
Then update the database URL in models.py to point to your 
database. 
Then run: python manage.py db init.
This will set up your database. 

to run the server run:
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

## Endpoints 
All but '/' and '/home' endpoints return JSON Objects.

Endpoints:
GET '/'
GET '/home'
GET '/blog_posts'
GET '/users'
GET '/users/{user_id}/blog_posts'
GET '/blog_posts/{blog_id}'
POST '/blog_posts'
POST '/users'
DELETE '/blog_posts/{blog_id}
PATCH '/blog_posts/{blog_id}'


```
GET '/'
this endpoint redirects to the auth0 login page

GET '/home' 
This endpoint just exists as a landing page.

GET '/blog_posts'
- Returns a JSON of all the blog posts
- Request Arguments: none
- Permissions Required: none
- Returns whether it was successful and all the blog posts: {
    success: true,
    blogs: [
        {
            id: 1,
            title: 'My first blog post',
            body: 'This is my first blog post, I hope you like it',
            author_id: 1
        }
    ]
}

GET '/users'
- Returns a list of all the users.
- Request Arguments: none
- Permissions required: get:users
- Returns whether it was successful and all the users: {
    sucess:true,
    users:[
        {
            id: 1,
            name: 'John Smith',
            email: 'JSmith@email.com',
            blog_posts: [
                {
                    id: 1,
                    title: 'My first blog post',
                    body: 'This is my first blog post, I hope you like it',
                    author_id: 1
                }
            ]
        }
    ]
}

GET '/users/{user_id}/blog_posts'
- Returns all the blog posts for the specified user
- Request Arguments: none
- Permissions Required: get:users
- Returns whether it was successful, the user id, the total number of blogs associated with the user, and all the blogs associated with that user: {
    sucess: true,
    user: 1,
    blogs:[
        {
            id: 1,
            title: 'My first blog post',
            body: 'This is my first blog post, I hope you like it',
            author_id: 1
        }
    ],
    total_blogs: 1
}

GET '/blog_posts/{blog_id}'
- Returns the blogpost connected to the ID
- Request Arguments: none
- Permissions Required: none
- Returns whether it was successful and the blogpost: {
    success:true,
    {
        id: 1,
        title: 'My first blog post',
        body: 'This is my first blog post, I hope you like it',
        author_id: 1
    }
} 

POST '/blog_posts'
- Creates a new blog post
- Request Arguments: a JSON object with a title, body and author id. The 
    {
        title: 'My title',
        body: 'This is the body of my blog',
        author_id: 1
    }
- Permissions Required: post:blog_posts
- Returns whether it was successful and the id of the created blog post:
{
    success: true, 
    created: 2
}

POST '/users'
- Creates a new user
- Request Arguments: A JSON object with a name and an email,
    {
        name: 'Joe Shmoe',
        email: 'JShoe@email.com'
    }
- Permissions Required: post:users
- Returns whether it was succesful and the id of the created user:
{
    success: true,
    created: 2
}

DELETE '/blog_posts/{blog_id}'
- Deletes the specified blog post
- Request Arguments: none
- Permissions Required: delete: blog_posts
- Returns whether it was deleted or not and the id of the deleted blog post: 
    {
        success: true,
        deleted: 2
    } 

PATCH '/blog_posts/{blog_id}
- Updates the specified blog post
- Request Arguments: a JSON object with either a title or body. Either may be null if only one wants to be updated. 
    {
        title: 'my new title',
        body: 'my new body'
    }
- Permissions Required: patch:blog_posts
- Returns whether it was successful and the new blog post:
    {
        success: true,
        blog_post: [
            id: 1,
            title: 'my new title',
            body: 'my new body',
            author_id: 1
        ]
    }