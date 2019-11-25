import pytest
from books.db_engine import DbEngine


@pytest.fixture(scope='session')
def db_engine():
    db_engine = DbEngine()
    yield db_engine
    db_engine.db_engine.dispose()


@pytest.fixture(scope='function')
def database(db_engine):
    db_engine.create_all()
    yield db_engine
    db_engine.drop_all()


@pytest.fixture(scope='function')
def session_maker(database):
    yield database.session_maker
