import urllib.request,json
from .models import Sources, Articles


# Getting api key
api_key = None
# Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url,news_api_sources_url,news_api_articles_url
    api_key = app.config['NEWS_API_KEY']
    news_api_articles_url = app.config['NEWS_API_ARTICLES_URL']
    news_api_sources_url = app.config['NEWS_API_SOURCES_URL']

def get_articles(sources_id):
    '''
    Function that gets the json results to our url request
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=bb900c6b52db42d0a4cd6a8b422b91a9'.format(sources_id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)


    return articles_results

def process_articles(articles_list):
    '''
    Function that processes the articles result and transform them to a list of article objects

    Args:
        articles_list:A list of dictionaries that contains articles details

    Returns:
        articles_results:A list of articles objects
    '''
    articles_results = []
    for articles_item in articles_list:
        title = articles_item.get('title')
        urlToImage = articles_item.get('urlToImage')
        content = articles_item.get('content')
        author = articles_item.get('author')
        publishedAt = articles_item.get('publishedAt')
        url = articles_item.get('url')
        # import pdb
        # pdb.set_trace()
        if title:
            articles_object = Articles(title,content,urlToImage,author,publishedAt,url)
            articles_results.append(articles_object)

    return articles_results