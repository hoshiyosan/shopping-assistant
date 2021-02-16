from .helpers import HTTPSession

session = HTTPSession("http://localhost:8000")



ACCOUNTS = [
    {"email": "admin", "password": "toto"}
]

accounts = {}
for account_data in ACCOUNTS:
    accounts[account_data["email"]] = session.post("/accounts", json=account_data).json()



admin_access_token = session.post("/auth/token", json=ACCOUNTS[0]).json()["access_token"]
authorization = {"Authorization": f"Bearer {admin_access_token}"}


INGREDIENTS = [
    {"name": "Poulet", "unit": "grammes", "category": "Viandes"},
    {"name": "Poivrons", "unit": None, "category": "Fruits et Légumes"},
    {"name": "Oignons", "unit": None, "category": "Fruits et Légumes"},
    {"name": "Lardons", "unit": "grammes", "category": "Viandes"},
    {"name": "Crème fraîche", "unit": "millilitres", "category": "Laitages"}
]

ingredients = {}
for ingredient_data in INGREDIENTS:
    ingredients[ingredient_data["name"]] = session.post("/ingredients", json=ingredient_data, headers=authorization).json()
