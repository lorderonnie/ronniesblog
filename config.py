import os

class Config:
    
    SECRET_KEY='prime'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ronald:1645@localhost/ronniesblog'       

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}