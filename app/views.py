from flask import render_template
from app import app

# Views

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    title = 'Home - Welcome to The best News preview articles'
    return render_template('index.html',title = title)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    Root function returning index/home page with data
    '''
    return render_template('news.html',id = news_id)
