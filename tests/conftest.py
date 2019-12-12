import pytest

from books import create_app

from books.db_engine import db


@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def _db(app):
    database = db
    database.drop_all()
    yield database


@pytest.fixture(scope='function')
def database(_db):
    _db.create_all()
    yield _db
    _db.drop_all()


@pytest.fixture(scope='function')
def session_maker(database):
    yield database.session_maker
