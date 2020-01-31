import click
import typing

from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

from books.settings.config import TestingConfig, config_for_environment
from books.settings import environment, user, host, port, dbname, options


sqla_db = SQLAlchemy()


#  Flask App Factory
def create_app(test_config: typing.Optional[TestingConfig]):
    app = Flask(__name__)

    # Configure the app according to environment
    if test_config is not None:
        app.config.from_object(test_config)
    else:
        app.config.from_object(config_for_environment(environment))

    # Initialize Flask-SQLAlchemy and the init-db command
    print(f'Initializing MySQL connection to mysql://{user}:***@{host}:{port}/{dbname}{options}...')
    sqla_db.init_app(app)
    app.cli.add_command(init_db_command)

    # Apply blueprints to the app
    from books.api import books
    app.register_blueprint(books)

    return app


def init_db():
    sqla_db.create_all()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """ Clear existing data and create new tables. """
    init_db()
    click.echo('Initialized the database.')
