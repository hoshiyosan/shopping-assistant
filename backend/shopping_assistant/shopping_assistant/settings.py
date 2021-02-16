from uuid import uuid4 as _uuid4
from os import getenv as _getenv

APP_ENCRYPTION_ALGORITHM = _getenv("APP_ENCRYPTION_ALGORITHM", "HS256")
APP_SECRET_KEY = _getenv("APP_SECRET_KEY", "d7da8827-b5d7-4820-9528-e501aa3ab787")
APP_CORS_ORIGINS = [
    "http://localhost:8080",
    "http://192.168.56.124:8080",
]

INGREDIENTS_UNITS = ('grammes', 'millilitres', 'kilogrammes', 'litres', 'cuillere à soupe', 'cuillère à café')
INGREDIENTS_CATEGORIES = ('Viande', 'Poisson', 'Fruits et Légumes', 'Epicerie sucrée', 'Epicerie salée', 'Boulangerie', 'Fromage')

SHOPPING_DATABASE_URI = _getenv("SHOPPING_DATABASE_URI", "mongodb://localhost:27017/shopping")
