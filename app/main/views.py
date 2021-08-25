from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():

    title = 'Blog App'

    return render_template('index.html'title = title)