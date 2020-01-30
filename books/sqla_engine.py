from contextlib import contextmanager

import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker, Session
from books.db import Base

import logging


class SqlaEngine:

    def __init__(self, host, port, dbname, user, password, rdms='mysql', options=''):
        uri = f'{rdms}://{user}:{password}@{host}:{port}/{dbname}{options}'
        print(f'Initializing MySQL connection to {rdms}://{user}:***@{host}:{port}/{dbname}{options}...')
        self._engine = sqla.create_engine(uri, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        if len(self.tables()) == 0:
            self.create_all()

    @contextmanager
    def session_scope(self):
        session: Session = self.session_maker()
        try:
            yield session
            session.commit()
        except Exception as e:
            logging.error(f'{e}')
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def session_maker(self):
        return self._session_maker

    def create_all(self):
        Base.metadata.create_all(self._engine)

    def drop_all(self):
        Base.metadata.drop_all(self._engine)

    def dispose(self):
        self._engine.dispose()

    def init_app(self, app):
        app.teardown_appcontext(self.dispose())

    def tables(self):
        return self._engine.table_names()
