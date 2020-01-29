import os
from books.sqla_engine import SqlaEngine

host = os.getenv('MYSQL_HOST', '127.0.0.1')
port = int(os.getenv('MYSQL_PORT', '3306'))
dbname = os.getenv('MYSQL_DBNAME', 'books')
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', 'password')

sqla_engine = SqlaEngine(host, port, dbname, user, password)
