import urllib.request,json
from .models import Sources, Articles


# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url,news_api_sources_url,news_api_articles_url
    api_key = app.config['NEWS_API_KEY']
    news_api_sources_url = app.config['NEWS_API_SOURCES_URL']
    news_api_articles_url = app.config['NEWS_API_ARTICLES_URL']
