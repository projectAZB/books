
from flask import request, Response, Blueprint
from books.book_db_api import BookDbApi

from books.db_engine import db


books = Blueprint('books', __name__, url_prefix='/books')


@books.route('/create', methods=['POST'])
def create_book():
    json_body = request.get_json(force=True)
    if all(key in json_body for key in ('title', 'author', 'genre')):
        book_db_api = BookDbApi(db.session_maker)
        book_db_api.create_book(json_body.get('title'), json_body.get('author'), json_body.get('genre'))
    else:
        return Response(status=400)
    return Response()
