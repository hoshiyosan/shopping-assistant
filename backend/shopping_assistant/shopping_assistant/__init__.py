from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from shopping_assistant import domain
from shopping_assistant.settings import APP_CORS_ORIGINS

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=APP_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(domain.authnz.router, tags=["Authentication"])
api.include_router(domain.accounts.router, tags=["Accounts"])

api.include_router(domain.ingredients.router, tags=["Ingredients"])
api.include_router(domain.recipes.router, tags=["Recipes"])
