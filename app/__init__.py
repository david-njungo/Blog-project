from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_moment import Moment


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)

    #initialize flask extensions
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    #Register the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app