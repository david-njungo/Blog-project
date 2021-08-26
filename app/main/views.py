from flask import render_template,request,redirect,url_for
from . import main
# from ..request import get_quotes

@main.route('/')
def index():
#     quote = get_quotes('random')

    return render_template('index.html')

