class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL="https://newsapi.org/v2/everything?q=tesla&from=2021-09-30&sortBy=publishedAt&apiKey=1dac542d43124d64a55021524dac25b4"



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