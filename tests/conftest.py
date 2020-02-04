import pytest

from books import create_app, sqla_db
from books.settings.config import TestingConfig


@pytest.fixture(scope='session', autouse=True)
def app():
    app = create_app(TestingConfig())
    yield app


@pytest.fixture(scope='function', autouse=True)
def database(app):
    with app.test_request_context():
        sqla_db.drop_all()
        sqla_db.create_all()
        yield
        sqla_db.session.remove()
