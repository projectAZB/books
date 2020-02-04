from abc import ABC

from books.settings.environment import Environment
from . import db_url


class BaseConfig(ABC):
    FLASK_ADMIN_SWATCH = 'cerulean'
    SECRET_KEY = 'shhh'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Set to silence warnings
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'pool_pre_ping': True
    }


class TestingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


_configs = {
    Environment.TESTING: TestingConfig(),
    Environment.DEVELOPMENT: DevelopmentConfig(),
    Environment.STAGING: StagingConfig(),
    Environment.PRODUCTION: ProductionConfig()
}


def config_for_environment(environment: Environment):
    return _configs[environment]