from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    view page functions that returns an index page and its data
    '''
    
    title = 'News Highlight application'
    return render_template('index.html',title = title)


@app.route('/news/<int:news_id>')
def news(news_id):
    '''
     view page that returns news details and its data
    '''

    return render_template('news.html',id = news_id)