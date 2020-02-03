#!/bin/bash -e

# access-logfile: `-` signifies stdout
# error-logfile: `-` signifies stderr
gunicorn -w 1 --bind :5000 --access-logfile - --error-logfile - "books:create_app()"
