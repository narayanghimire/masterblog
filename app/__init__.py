import os

from flask import Flask


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates'),
        static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')
    )

    # Register the blog blueprint
    from app.controller.blog_controller import  blog_bp
    app.register_blueprint(blog_bp)

    return app
