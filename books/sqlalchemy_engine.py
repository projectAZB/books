import os

import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker
from books.book_db import Base


class SqlAlchemyEngine:

    def __init__(
            self,
            host='127.0.0.1',
            port=3306,
            dbname='books_test',
            dbuser='root',
            password='password',
            rdms='mysql'
    ):
        uri = f'{rdms}://{dbuser}:{password}@{host}:{port}/{dbname}'
        print(f'Initializing MySQL connection to {uri}...')
        self._engine = sqla.create_engine(uri, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        if len(self.tables()) == 0:
            self.create_all()

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


db = SqlAlchemyEngine(
    os.getenv('MYSQL_HOST', '127.0.0.1'),
    int(os.getenv('MYSQL_PORT', '3306')),
    os.getenv('MYSQL_DBNAME', 'books'),
    os.getenv('MYSQL_USER', 'root'),
    os.getenv('MYSQL_PASSWORD', 'password')
)
