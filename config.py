import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'trantrungnhat'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = bool(os.environ.get('MAIL_USE_TLS')) or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'trungnhatnd1996@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'bsbmjsyzklyeuvhr'
    BLOG_MAIL_SUBJECT_PREFIX = '[BlogTTN]'
    BLOG_MAIL_SENDER = '[BlogTTN] Admin <trungnhatnd1996@gmail.com>'
    BLOG_ADMIN = os.environ.get('BLOG_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ITSDANGEROUS_SECRET_KEY = os.environ.get('SECRET_KEY_ITSDANGEROUS') or 'trantrungnhat'
    ITSDANGEROUS_EXPIRATION = int(os.environ.get('ITSDANGEROUS_EXPIRATION', 3600))  # s

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://root:Wakerjacob@90@localhost' \
                                                                    ':3306/blog'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
