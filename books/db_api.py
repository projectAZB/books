import typing

from books import sqla_db
from books.db import Book as BookRec
from books.dao import Book


class DbApi:

    @staticmethod
    def create_book(title: typing.AnyStr, author: typing.AnyStr, genre: typing.AnyStr) -> Book:
        new_book = Book(title, author, genre)
        new_book_rec: BookRec = new_book.to_book_rec()
        sqla_db.session.add(new_book_rec)
        sqla_db.session.commit()
        return new_book

    @staticmethod
    def get_book(title: typing.AnyStr, author: typing.Optional[typing.AnyStr] = None) -> Book:
        if author is None:
            book_rec = sqla_db.session.query(BookRec).filter(BookRec.title == title).one()
        else:
            book_rec = sqla_db.session.query(BookRec).filter(BookRec.title == title, BookRec.author == author).one()
        book = Book.from_book_rec(book_rec)
        return book

    @staticmethod
    def get_all_books() -> typing.List[Book]:
        book_recs = sqla_db.session.query(BookRec).all()
        books = list(map(lambda book_rec: Book.from_book_rec(book_rec), book_recs))
        return books
