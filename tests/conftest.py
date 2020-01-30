import pytest

from books import create_app, sqla_db
from books.config import TestingConfig


@pytest.fixture(scope='session', autouse=True)
def app():
    app = create_app(TestingConfig())
    with app.app_context():
        yield app
    sqla_db.session.remove()


@pytest.fixture(scope='function', autouse=True)
def database(app):
    sqla_db.drop_all()
    sqla_db.create_all()
    yield


@pytest.fixture(scope='function', autouse=True)
def session(database):
    yield
    sqla_db.session.remove()
