from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] == "hsbabagakas iahaha sis sis siw wiw wka sis x xbzbz sb"
    
    from .view import views
    
    app.register_blueprint(views, url_prefix="/")
    
    return app