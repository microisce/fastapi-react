import os

PROJECT_NAME = "bookstore"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URI:
    os.putenv('DATABASE_URL', 'sqlite:///bookstore.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bookstore.db'

API_V1_STR = "/api/v1"
