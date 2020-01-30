import typing

from books.sqla_engine import SqlaEngine

from books.db import Book as BookRec
from books.book import Book


class DbApi:

    def __init__(self, sql_engine: SqlaEngine):
        self.sql_engine = sql_engine

    def create_book(
            self,
            title: typing.AnyStr,
            author: typing.AnyStr,
            genre: typing.AnyStr
    ) -> Book:
        with self.sql_engine.session_scope() as session:
            new_book = Book(title, author, genre)
            new_book_rec: BookRec = new_book.to_book_rec()
            session.add(new_book_rec)
        return new_book

    def get_book(self, title: typing.AnyStr, author: typing.Optional[typing.AnyStr] = None) -> Book:
        with self.sql_engine.session_scope() as session:
            if author is None:
                book_rec = session.query(BookRec).filter(BookRec.title == title).one()
            else:
                book_rec = session.query(BookRec).filter(BookRec.title == title, BookRec.author == author).one()
            book = Book.from_book_rec(book_rec)
        return book

    def get_all_books(self) -> typing.List[Book]:
        with self.sql_engine.session_scope() as session:
            book_recs = session.query(BookRec).all()
            books = list(map(lambda book_rec: Book.from_book_rec(book_rec), book_recs))
        return books

