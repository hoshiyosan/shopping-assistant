from os import getenv as _getenv

INGREDIENTS_UNITS = ('grammes', 'millilitres', 'kilogrammes', 'litres', 'cuillere à soupe', 'cuillère à café')
INGREDIENTS_CATEGORIES = ('Viande', 'Poisson', 'Fruits et Légumes', 'Epicerie sucrée', 'Epicerie salée', 'Boulangerie', 'Fromage')

SHOPPING_DATABASE_URI = _getenv("SHOPPING_DATABASE_URI", "mongodb://localhost:27017/shopping")
