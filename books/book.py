import typing
from books.book_db import Book as BookRec


class Book:
    """DAO for BookRec"""

    def __init__(self, title: typing.AnyStr, author: typing.AnyStr, genre: typing.AnyStr):
        self.title = title
        self.author = author
        self.genre = genre

    def to_book_rec(self):
        return BookRec(title=self.title, author=self.author, genre=self.genre)

    @staticmethod
    def from_book_rec(book_rec: BookRec):
        return Book(title=book_rec.title, author=book_rec.author, genre=book_rec.genre)
