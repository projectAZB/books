import typing
import logging

from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

from books.book_db import Book as BookRec
from books.book import Book


class BookDbApi:

    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    @contextmanager
    def session_scope(self):
        session: Session = self.session_maker()
        try:
            yield session
            session.commit()
        except Exception as e:
            logging.error(f'{e}')
            session.rollback()
        finally:
            session.close()

    def create_book(
            self,
            title: typing.AnyStr,
            author: typing.AnyStr,
            genre: typing.AnyStr
    ) -> Book:
        with self.session_scope() as session:
            new_book = Book(title, author, genre)
            new_book_rec: BookRec = new_book.to_book_rec()
            session.add(new_book_rec)
        return new_book

    def get_book(self, title: typing.AnyStr) -> Book:
        with self.session_scope() as session:
            book_rec = session.query(BookRec).filter(BookRec.title == title).first()
            book = Book.from_book_rec(book_rec)
        return book

    def get_all_books(self) -> typing.List[Book]:
        with self.session_scope() as session:
            book_recs = session.query(BookRec).all()
            books = list(map(lambda book_rec: Book.from_book_rec(book_rec), book_recs))
        return books

