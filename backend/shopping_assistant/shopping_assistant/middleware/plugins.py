from pymongo import MongoClient
from ..settings import SHOPPING_DATABASE_URI


mongo = MongoClient(SHOPPING_DATABASE_URI)
