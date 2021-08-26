from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    quotes = get_quotes('9')

    return render_template('index.html',quotes = quotes)

