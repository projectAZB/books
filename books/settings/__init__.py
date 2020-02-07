import os

# Extract env variables here

environ = int(os.getenv('ENVIRONMENT', 1))  # Default to Development (1)

host = os.getenv('MYSQL_BOOKS_HOST', '127.0.0.1')
port = int(os.getenv('MYSQL_BOOKS_PORT', '3306'))
dbname = os.getenv('MYSQL_BOOKS_DBNAME', 'books')
test_dbname = os.getenv('MYSQL_BOOKS_TEST_DBNAME', 'books-test')
user = os.getenv('MYSQL_BOOKS_USER', 'root')
password = os.getenv('MYSQL_BOOKS_PASSWORD', 'password')

db_url = f'mysql://{user}:{password}@{host}:{port}/{dbname}'
test_db_url = f'mysal://{user}:{password}@{host}:{port}/{dbname}'
