from fastapi import APIRouter
from shopping_assistant.settings import INGREDIENTS_UNITS, INGREDIENTS_CATEGORIES
from typing import List
from .schemas import Ingredient
from .database import IngredientsDatabase


router = APIRouter()
ingredients_db = IngredientsDatabase()


@router.get("/ingredients/units")
def list_ingredients_units():
    return INGREDIENTS_UNITS


@router.get("/ingredients/categories")
def list_ingredients_categories():
    return INGREDIENTS_CATEGORIES


@router.get("/ingredients/{ingredient_uid}", response_model=Ingredient)
def get_ingredient(ingredient_uid: str):
    return ingredients_db.get(ingredient_uid)


@router.get("/ingredients", response_model=List[Ingredient])
def search_ingredients():
    return ingredients_db.search()


@router.post("/ingredients", response_model=Ingredient)
def create_ingredient(ingredient: Ingredient):
    return ingredients_db.create(ingredient)


@router.put("/ingredients/{ingredient_uid}", response_model=Ingredient)
def update_ingredient(ingredient_uid: str, ingredient: Ingredient):
    return ingredients_db.update(ingredient_uid, ingredient)


@router.delete("/ingredients/{ingredient_uid}", response_model=Ingredient)
def delete_ingredient(ingredient_uid: str):
    return ingredients_db.delete(ingredient_uid)
