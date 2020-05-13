import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import Blog_Post, User, setup_db, db
from flask_migrate import Migrate
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    migrate = Migrate(app,db)

    '''
        The after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    '''
        Gets the json body for the request. 
        If there is no json, then it throws an error.
    '''
    def get_body(request):
        body = request.get_json()
        if body is None:
            abort(400)
        return body

    # A GET endpoint to get all the blog posts
    @app.route('/blog_posts', methods=['GET'])
    def get_all_blog_posts():
        blog_posts = Blog_Post.query.all()
        return jsonify({
            'success': True,
            'blogs': [blog.format() for blog in blog_posts]
        })

    # A GET endpoint to get all the users
    @app.route('/users', methods=['GET'])
    def get_all_users():
        users = User.query.all()
        return jsonify({
            'success': True,
            'users': users
        })

    """
        A GET endpoint to get all the blogposts for a specific user. 
    """
    @app.route('/users/<int:user_id>/blog_posts', methods=['GET'])
    def get_all_posts_for_user(user_id):
        blog_posts = Blog_Post.query.filter(
            Blog_Post.author_id == user_id).all()
        if(blog_posts is None or len(blog_posts) == 0):
            abort(404)

        return jsonify({
            'success': True,
            'user': user_id,
            'blogs': [blog.format() for blog in blog_posts],
            'total_blogs': len(blog_posts)
        })

    # A GET endpoint to get a specific blog post
    @app.route('/blog_posts/<int:blog_post_id>', methods=['GET'])
    def get_blog_post(blog_post_id):
        blog_post = Blog_Post.query.filter(
            Blog_Post.id == blog_post_id).one_or_none()
        if (blog_post is None):
            abort(404)

        return jsonify({
            'success': True,
            'blog_post': blog_post.format()
        })

    # A POST endpoint used to create new blog posts. 
    @app.route('/blog_post', methods=['POST'])
    def create_blog_post():
        body = get_body(request)
        try:
            title = body.get('title', None)
            body = body.get('body', None)
            author_id = body.get('author_id', None)
        except:
            abort(401)

        try:
            new_blog_post = Blog_Post(title, body, author_id)
            new_blog_post.insert()

            return jsonify({
                'success': True,
                'created': new_blog_post.id,
            })
        except:
            abort(422)

    # A POST endpoint used to create new users. 
    @app.route('/users', methods=['POST'])
    def create_user():
        body = get_body(request)
        try:
            name = body.get('name', None)
            email = body.get('email', None)
        except:
            abort(401)

        try:
            new_user = User(name, email)
            new_user.insert()

            return jsonify({
                'success': True,
                'created': new_user.id,
            })
        except:
            abort(422)

    # A DELETE endpoint used to delete blog posts
    @app.route('/blog_post/<int:blog_id>', methods=['DELETE'])
    def delete_blog_post(blog_id):
        blog_post = Blog_Post.query.filter(Blog_Post.id == blog_id).one_or_none()
        if(blog_post is None):
            abort(404)
        
        try:
            blog_post.delete()
            return jsonify({
                'success': True,
                'deleted': blog_id,
            })
        except:
            abort(422)
    
    #A PATCH endpoint used to update blog posts
    @app.route('/blog_post/<int:blog_id', methods=['PATCH'])
    def update_blog_post(blog_id):
        blog_post = Blog_Post.query.filter(Blog_Post.id == blog_id).one_or_none()
        if(blog_post is None):
            abort(404)
        
        body = get_body(request)

        title = body.get('title')
        blog_body = body.get('body')
        
        try:
            if(title is not None):
                blog_post.title = title
            
            if(blog_body is not None):
                blog_post.body = blog_body
            
            blog_post.update()
            return jsonify({
                'success': True
            })
        except:
            abort(422)
        
    

    @app.errorhandler(400)
    def bad_request(error):
        return handle_error(400, 'Bad request')

    @app.errorhandler(404)
    def not_found(error):
        return handle_error(404, 'Not found')

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return handle_error(422, 'Unprocessable entity')

    def handle_error(code, message):
        return jsonify({
            'success': False,
            'error': code,
            'message': message
        }), code

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
