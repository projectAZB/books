
# Creates a layer (the base image) from the Debian Buster 'python:3.7-buster' Docker image
FROM python:3.7-buster

RUN mkdir -p /app/books/
WORKDIR /app/

RUN apt-get update -y && apt-get install -y default-mysql-client default-libmysqlclient-dev

COPY ./requirements.txt /app/
COPY ./wheelhouse /app/wheelhouse
COPY ./start.sh /app/
COPY ./books /app/books/

RUN pip install -r requirements.txt

RUN chmod 755 start.sh

EXPOSE 5000

CMD ["./start.sh"]
