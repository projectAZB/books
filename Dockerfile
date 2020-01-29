# Dockerfile - Text document that contains all the commands a user could call on the command line to assemble an image.
# Using `docker build` users can create an automated build that executes several command-line instructions in succesion.
# `docker build` builds an image from a Dockerfile AND a context. The build's context is the set of files at a specified
# location PATH or URL. PATH is a directory on your local filesystem, and URL is a Git repository location

# The build is run by the Docker daemon, not by the CLI. The first thing the build process does is send the entire
# context (recursively) to the daemon.
# It's best to start with an empty directory as context and keep your Dockerfile in that directory (only what's needed)

# DO NOT use your root directory `/` as the PATH as it causes the build to transfer the entire contents of your hard
# drive to the daemon

# Creates a layer (the base image) from the Debian Buster 'python:3.7-buster' Docker image
FROM python:3.7-buster

RUN mkdir -p /app/
WORKDIR /app/

COPY . /app

