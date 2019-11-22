import pytest
from books.db_engine import DbEngine


@pytest.fixture(scope='function')
def engine():
    db_engine = DbEngine()
    db_engine.create_all()
    yield db_engine
    db_engine.drop_all()
    db_engine.db_engine.dispose()


@pytest.fixture(scope='function')
def session_maker(engine):
    yield engine.session_maker
