from app import app
import urllib.request,json
from .models import news

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results  

def process_results(news_list):
        '''
        Function  that processes the news result and transform them to a list of Objects
        '''

        news_results = []
        for news_item in news_list:
            id = news_item.get('id')
            name = news_item.get('name')
            description = news_item.get('description')

            news_object = News(id,name,description)
            news_results.append(news_object)

        return news_results   

def get_new(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')

            news_object = News(id,name,description)

    return news_object

            
       