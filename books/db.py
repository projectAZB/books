from sqlalchemy import UniqueConstraint

from books import sqla_db


class Book(sqla_db.Model):
    __table_args__ = (UniqueConstraint('title', 'author', name='_title_author_uc'),)

    id = sqla_db.Column(sqla_db.Integer, primary_key=True)
    title = sqla_db.Column(sqla_db.String(250), nullable=False, index=True)
    author = sqla_db.Column(sqla_db.String(250), nullable=False)
    genre = sqla_db.Column(sqla_db.String(250))
