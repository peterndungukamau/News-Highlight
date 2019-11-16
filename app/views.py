from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    view page functions that returns an index page and its data
    '''

    return render_template('index.html')