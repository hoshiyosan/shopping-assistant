from fastapi import FastAPI
from shopping_assistant import domain

api = FastAPI()

api.include_router(domain.authnz.router, tags=["Authentication"])
api.include_router(domain.accounts.router, tags=["Accounts"])

api.include_router(domain.ingredients.router, tags=["Ingredients"])
api.include_router(domain.recipes.router, tags=["Recipes"])
