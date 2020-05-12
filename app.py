import os
from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from models import Blog_Post, User, setup_db
from flask_migrate import Migrate
from auth import AuthError, requires_auth


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/blog_posts', methods=['GET'])
    def get_all_blog_posts():
        blogs = Blog_Post.query.all()
        return jsonify({
            'success': True, 
            'blogs': {blog.title:blog.body for blog in blogs}
        })

    @app.route('/users', methods=['GET'])
    def get_all_users():
        users = User.query.all()
        return jsonify({
            'success':True,
            'users': users
        })

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
            'success':False,
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