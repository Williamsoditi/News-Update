from flask import render_template
from ..requests import get_articles, get_sources
from . import main

#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting news sources
    sources = get_sources()
    title = 'News Updates'

    return render_template('index.html',title = title, sources = sources)

@main.route('/articles/<sources_id>')
def articles(sources_id):
    '''
    View articles page function that returns article details page and the data in it
    '''
    articles = get_articles(sources_id)
    
    return render_template('articles.html',articles = articles)

