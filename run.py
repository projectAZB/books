import os

from flask import Flask, request, Response
from books.db_engine import DbEngine
from books.book_db_api import BookDbApi


app = Flask(__name__)

db = DbEngine(
    os.getenv('MYSQL_HOST', '127.0.0.1'),
    os.getenv('MYSQL_PORT', '3306'),
    os.getenv('MYSQL_DBNAME', 'book_db'),
    os.getenv('MYSQL_USER', 'root'),
    os.getenv('MYSQL_PASSWORD', 'password')
)


@app.route('/create_book', methods=['POST'])
def create_book():
    json_body = request.get_json(force=True)
    if all(key in json_body for key in ('title', 'author', 'genre')):
        book_db_api = BookDbApi(db.session_maker)
        book_db_api.create_book(json_body.get('title'), json_body.get('author'), json_body.get('genre'))
    else:
        return Response(status=400)
    return Response()
