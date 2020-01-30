import pytest

from books import create_app
from books import settings


@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def _sqla_engine(app):
    sqla_engine = settings.sqla_engine
    sqla_engine.drop_all()
    yield sqla_engine


@pytest.fixture(scope='function')
def sqla_engine(_sqla_engine):
    _sqla_engine.create_all()
    yield _sqla_engine
    _sqla_engine.drop_all()
