import sqlalchemy as sqla

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String(250), nullable=False)
    author = sqla.Column(sqla.String(250), nullable=False)
    genre = sqla.Column(sqla.String(250))
