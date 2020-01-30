
from flask import Response

from books.db_api import DbApi


class TestBookApi:

    def test_create_book_api(self, app):
        with app.test_client() as context:
            response: Response = context.post('/books/create', json={
                'title': 'Pnin',
                'author': 'Vladimir Nabokov',
                'genre': 'Campus'
            })
            assert response.status_code == 200
            response: Response = context.post('/books/create', json={
                'title': 'Demian',
                'author': 'Hermann Hesse',
                'genre': 'Fiction'
            })
            assert response.status_code == 200
            assert len(DbApi.get_all_books()) == 2

            response: Response = context.get('/books?title=Pnin&author=Vladimir%20Nabokov')
            assert response.status_code
            json_body = response.get_json(force=True)
            assert json_body.get('title') == 'Pnin'
            assert json_body.get('author') == 'Vladimir Nabokov'
            assert json_body.get('genre') == 'Campus'

            response: Response = context.get('/books?title=Demian&author=Hermann%20Hesse')
            assert response.status_code
            json_body = response.get_json(force=True)
            assert json_body.get('title') == 'Demian'
            assert json_body.get('author') == 'Hermann Hesse'
            assert json_body.get('genre') == 'Fiction'

            response: Response = context.post('/books/create', json={
                'title': 'Demian',
                'author': 'Hermann Hesse',
                'genre': 'Fiction'
            })
            assert response.status_code != 200
