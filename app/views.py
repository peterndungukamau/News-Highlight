from flask import render_template
from app import app
from .request import get_news,get_new

@app.route('/')
def index():
    '''
    view page functions that returns an index page and its data
    '''
    
    latest_news = get_news('latest')
    title = 'News Highlight application'
    return render_template('index.html',title = title,latest = latest_news)


@app.route('/new/<int:id>')
def new(id):
    '''
     view page that returns news details and its data
    '''

    new = get_new(id)
    title = f'{new.title}'
 
    return render_template('news.html',title = title,new = new)


