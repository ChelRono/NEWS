class Config:
    '''
    General configuration parent class
    '''
    pass

    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?language=en&q=tesla&from=2022-04-05&sortBy=publishedAt&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True