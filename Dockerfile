# Creates a layer (the base image) from the Debian Buster 'python:3.7-buster' Docker image
FROM python:3.7-buster

RUN mkdir -p /app/
WORKDIR /app/

RUN apt-get update -y && apt-get install -y default-mysql-client default-libmysqlclient-dev

COPY ./requirements.txt /app/
COPY ./wheelhouse /app/wheelhouse/

RUN pip install -r requirements.txt -f wheelhouse

COPY . /app/

ENV PYTHONPATH=/app/
