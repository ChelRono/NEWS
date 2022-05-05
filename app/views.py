from flask import render_template
from app import app
from .request import get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    articles = get_articles('articles')
    title='Welcome to the best news website'
    return render_template('index.html', title=title, articles=articles)

@app.route('/articles/<string:id>')
def articles(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('articles.html',id= id)