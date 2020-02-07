import click
import typing
import logging

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

from books.settings.config import TestingConfig, config_for_environment
from books.settings import environ, user, host, port, dbname


sqla_db = SQLAlchemy()


#  Flask App Factory
def create_app(test_config: typing.Optional[TestingConfig] = None):
    app = Flask(__name__)

    # Configure the app according to environment
    if test_config is not None:
        app.config.from_object(test_config)
    else:
        app.config.from_object(config_for_environment(environ))

    # Initialize Flask-SQLAlchemy and the init-db command
    print(f'Initializing MySQL connection to mysql://{user}:***@{host}:{port}/{dbname}...')
    sqla_db.init_app(app)
    app.cli.add_command(init_db_command)

    # Apply blueprints to the app
    from books.api import books
    app.register_blueprint(books)

    # Create a consistent logging experience, using Gunicorn logging level as the source of truth
    # Otherwise there is a discrepancy b/w Flask and Gunicorn log levels
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    return app


def init_db():
    sqla_db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """ Clear existing data and create new tables. """
    init_db()
    click.echo('Initialized the database.')
