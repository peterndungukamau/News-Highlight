class Config:
    '''
    General configuration class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY = '15679fa5c139429aa745a9ade048cd83'
    

class ProdConfig(Config):
    '''
    Production  configuration class
    '''   

    pass 

class DevConfig(Config):
    '''
    Development  configuration class
    '''    

    DEBUG = True

config_options = {
    'production' : ProdConfig,
    'development' : DevConfig
}