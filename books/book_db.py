import sqlalchemy as sqla

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UniqueConstraint

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    __table_args__ = (UniqueConstraint('title', 'author', name='_title_author_uc'),)

    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String(250), nullable=False, index=True)
    author = sqla.Column(sqla.String(250), nullable=False)
    genre = sqla.Column(sqla.String(250))
