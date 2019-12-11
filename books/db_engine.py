import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker
from books.book_db import Base


class DbEngine:

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
        self._engine = sqla.create_engine(uri, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        self.create_all()

    @property
    def session_maker(self):
        return self._session_maker

    @property
    def db_engine(self):
        return self._engine

    def create_all(self):
        Base.metadata.create_all(self._engine)

    def drop_all(self):
        Base.metadata.drop_all(self._engine)
