# Dockerfile - Text document containing all the commands a user could call on the command line to assemble an image.
# Using `docker build` users can create an automated build that executes several command-line instructions in succesion.
# `docker build` builds an image from a Dockerfile AND a context. The build's context is the set of files at a specified
# location PATH or URL. PATH is a directory on your local filesystem, and URL is a Git repository location

# The build is run by the Docker daemon, not by the CLI. The first thing the build process does is send the entire
# context (recursively) to the daemon.

# Creates a layer (the base image) from the Debian Buster 'python:3.7-buster' Docker image
FROM python:3.7-buster

RUN mkdir -p /app/books/
WORKDIR /app/

RUN apt-get update -y && apt-get install -y default-mysql-client default-libmysqlclient-dev

COPY ./books /app/books/

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["./start.sh"]
