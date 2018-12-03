import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = True
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is necessary to be change'
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/microblog_dev"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') #export DATABASE_URL="postgresql://localhost/microblog_dev"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mrzendo9x@gmail.com']
    SECURITY_EMAIL_SENDER = 'valid_email@my_domain.com'
    POSTS_PER_PAGE = 3
    # MAIL_SERVER=smtp.googlemail.com
    # MAIL_PORT=587
    # MAIL_USE_TLS=1
    # MAIL_USERNAME=<your-gmail-username>
    # MAIL_PASSWORD=<your-gmail-password>

    # LANGUAGES = {'en': 'English', 'vn': 'Vietnamese'}
    LANGUAGES = ['en', 'es']
    # MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    MS_TRANSLATOR_KEY = ""
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')


    def test():
        print(SQLALCHEMY_DATABASE_URI)

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True    

class TestingConfig(Config):
    TESTING = True
