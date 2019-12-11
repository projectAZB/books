
from flask import Response

from books.book_db_api import BookDbApi


class TestBookApi:

    def test_create_book_api(self, app, session_maker):
        with app.test_client() as context:
            response: Response = context.post('/create_book', json={
                'title': 'Pnin',
                'author': 'Vladimir Nabokov',
                'genre': 'Campus'
            })
            assert response.status_code == 200
            response: Response = context.post('/create_book', json={
                'title': 'Demian',
                'author': 'Hermann Hesse',
                'genre': 'Fiction'
            })
            assert response.status_code == 200
            book_db_api: BookDbApi = BookDbApi(session_maker)
            assert len(book_db_api.get_all_books()) == 2
