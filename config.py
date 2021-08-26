import secrets
import os

class Config:
    FLASK_APP = 'FLASK_APP'
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex()
    BLOG_API = 'http://quotes.stormconsultancy.co.uk/quotes/{}'

class DevConfig(Config):
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("davidnjungo3@gmail.com")
    MAIL_PASSWORD = os.environ.get("njungokimani")
    FLASK_ENV ="FLASK_ENV"
    DATABASE = "blogdb"
    POSTGRES_USER = os.environ.get("moringa")
    POSTGRES_PASSWORD = os.environ.get("1234")
    SQLALCHEMY_DATABASE_URI ="postgresql+psycopg2://moringa:1234@localhost/blogdb"

class ProdConfig(Config):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = ""
   
    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'default': DevConfig
}