from flask import Flask, url_for
from flask_injector import FlaskInjector
from dependencies import configure

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    from app.controller.blog_controller import blog_bp
    app.register_blueprint(blog_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=True, port=5002)
