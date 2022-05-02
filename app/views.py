from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

   # Getting top news
    top_news = get_news('top_headlines')
    print(top_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title, top_headlines = top_news)

@app.route('/news/<int:news_id>')
def movie(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)