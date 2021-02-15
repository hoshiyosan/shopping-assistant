from pymongo import MongoClient
from .auth import Authentication
from ..settings import APP_SECRET_KEY, APP_ENCRYPTION_ALGORITHM, SHOPPING_DATABASE_URI

auth = Authentication(secret_key=APP_SECRET_KEY, encryption_algorithm=APP_ENCRYPTION_ALGORITHM)
mongo = MongoClient(SHOPPING_DATABASE_URI)
