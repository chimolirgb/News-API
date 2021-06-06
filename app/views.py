from flask import render_template,request,redirect,url_for
from app import app
from flask import render_template,request,redirect,url_for
from .request import get_source,article_source,get_category,get_headlines


# Views

@app.route('/')
def index():

  '''
  View root page function that returns the index page and its data
  '''

  #getting views
  source= get_source() 
  headlines = get_headlines()
  title = 'Home - Welcome to The best News preview articles'
  return render_template('index.html',title = title, sources=source,headlines = headlines)


@app.route('/article/<id>')
def article(id):


  '''
  Root function returning index/home page with data
  '''
  # title= 'Articles'
  articles = article_source(id)
  return render_template('article.html',articles= articles,id=id )

@app.route('/categories/<cat_name>')
def category(cat_name):
  '''
  function to return the categories.html page and its content
  '''
  category = get_category(cat_name)
  title = f'{cat_name}'
  cat = cat_name

  return render_template('categories.html',title = title,category = category, cat= cat_name)  
