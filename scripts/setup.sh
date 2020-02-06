#!/usr/bin/env bash

set -e

cd /app

./scripts/wait-for-it.sh "$MYSQL_BOOKS_HOST":"$MYSQL_BOOKS_PORT" --timeout=60 --strict -- echo "DB is ~up~!!!!"

# Create databases
mysql --host="$MYSQL_BOOKS_HOST" --port="$MYSQL_BOOKS_PORT" -u"$MYSQL_BOOKS_USER" -p"$MYSQL_BOOKS_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $MYSQL_BOOKS_DBNAME"
mysql --host="$MYSQL_BOOKS_HOST" --port="$MYSQL_BOOKS_PORT" -u"$MYSQL_BOOKS_USER" -p"$MYSQL_BOOKS_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $MYSQL_BOOKS_TEST_DBNAME"


# Makes sure that the database is up to date with the most recent revision
alembic upgrade head
