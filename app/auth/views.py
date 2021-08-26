from flask import render_template,redirect,url_for,flash
from . import auth
from .forms import LoginForm,RegistrationForm
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db

from .forms import LoginForm, RegistrationForm

# creating an auth instance
login_manager = LoginManager()
# login_manager.init_app(app)
login_manager.login_view = 'login'

# import models
from ..models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @auth.before_first_request
def create_tables():
    db.create_all()

@auth.route('/')
def index():
    return render_template('index.html')

@auth.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('auth.blogs'))
        print('Invalid username or password')
        return redirect(url_for('login'))

    return render_template('login.html', form=form)

@auth.route('/register', methods =  ['GET', 'POST'])
def register():

    form = RegistrationForm()

    # get the data
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # hash the password
        hashed_password = generate_password_hash(password, method="sha256")

        new_user = User(first_name=first_name, last_name=last_name, 
                        username=username, email=email, password=hashed_password)

        # send the data to a db
        db.session.add(new_user)
        db.session.commit()
        print("User added successfully")
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)