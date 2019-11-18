class Config:
    '''
    General configuration class
    '''

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    

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