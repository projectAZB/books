
from flask import request, Response, Blueprint, jsonify
from books.db_api import DbApi

from books.settings import sqla_engine


books = Blueprint('books', __name__, url_prefix='/books')


@books.route('', methods=['GET'])
def get_book():
    title = request.args.get('title', None)
    author = request.args.get('author', None)
    if not title:
        return Response(status=400)
    book_dp_api = DbApi(sqla_engine)
    book = book_dp_api.get_book(title, author)
    return jsonify(title=book.title, author=book.author, genre=book.genre)


@books.route('/create', methods=['POST'])
def create_book():
    json_body = request.get_json(force=True)
    if all(key in json_body for key in ('title', 'author', 'genre')):
        book_db_api = DbApi(sqla_engine)
        book_db_api.create_book(
            json_body.get('title'),
            json_body.get('author'),
            json_body.get('genre')
        )
    else:
        return Response(status=400)
    return Response()