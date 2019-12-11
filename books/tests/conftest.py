import pytest

import run as flask_app


@pytest.fixture(scope='session')
def app():
    app = flask_app.app
    return app


@pytest.fixture(scope='session')
def _db():
    database = flask_app.db
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
