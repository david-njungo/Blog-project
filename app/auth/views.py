from flask import render_template,redirect,url_for
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from flask_login import login_user,logout_user,login_required
from werkzeug.security import check_password_hash, generate_password_hash
from .. import db






@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    # check for validation
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user:
            # check the password
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('schedules'))
        print('Invalid username or password')
        # return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/signup', methods =  ['GET', 'POST'])
def signup():

    form = SignUpForm()

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
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)