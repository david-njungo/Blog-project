from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    def __repr__(self):
        return f'User {self.username}'


class Post(db.Model):
    __tablename__= "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    description = db.Column(db.String(), nullable=False)
    author = db.Column(db.String(), nullable=False)




class Quote:
    def __init__(self,id,quote):
        self.id = id
        self.quote = quote