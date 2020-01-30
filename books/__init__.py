from flask import Flask


def create_app():
    app = Flask(__name__)

    from books.api import books
    app.register_blueprint(books)

    return app

