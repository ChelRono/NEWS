
import urllib.request,json
from .models import Articles

# Articles = articles.Articles

# Getting api key
# Getting api key
apikey = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global apikey,base_url
    
    base_url = app.config['NEWS_API_BASE_URL']

# Getting the movie base url


def get_articles(apikey):
    '''
    Function that gets the json response to our url request
    '''

   
    get_articles_url = base_url.format('192d6b3e4ce546d9be71bba8d16f9196')
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)

    return articles_results


def process_article_results(articles_list):

    articles_results = []
    for article_item in articles_list:
        id=article_item.get('source.id')
        name=article_item.get('name')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')
        content=article_item.get('content')


        articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(articles_object)
    return articles_results



