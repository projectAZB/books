import os

# Extract env variables here

environment = int(os.getenv('ENVIRONMENT', 1))  # Default to Development (1)

host = os.getenv('MYSQL_HOST', '127.0.0.1')
port = int(os.getenv('MYSQL_PORT', '3306'))
dbname = os.getenv('MYSQL_DBNAME', 'books')
user = os.getenv('MYSQL_USER', 'root')
password = os.getenv('MYSQL_PASSWORD', 'password')
options = os.getenv('MYSQL_OPTIONS', '')

db_url = f'mysql://{user}:{password}@{host}:{port}/{dbname}{options}'
