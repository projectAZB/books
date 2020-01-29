import pytest

from books import create_app
from books.sqla_engine import SqlaEngine
from books import settings


@pytest.fixture(scope='session')
def app():
    app = create_app()
    return app


@pytest.fixture(scope='session')
def _db(app):
    with app.app_context():
        database = SqlaEngine(settings.host, settings.port, settings.dbname, settings.user, settings.password)
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
