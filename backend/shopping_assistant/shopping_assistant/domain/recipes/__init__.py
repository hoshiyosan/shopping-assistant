from typing import List
from fastapi import APIRouter
from shopping_assistant.dependencies import authenticated_account

from .schemas import Recipe, RecipeSummary
from .database import RecipesDatabase


router = APIRouter()
recipes_db = RecipesDatabase()


@router.get("/recipes/{recipe_uid}", response_model=Recipe, dependencies=[authenticated_account])
def get_recipe(recipe_uid: str):
    return recipes_db.get(recipe_uid)


@router.get("/recipes", response_model=List[RecipeSummary], dependencies=[authenticated_account])
def search_recipes():
    return recipes_db.search()


@router.post("/recipes", response_model=Recipe, dependencies=[authenticated_account])
def create_recipe(recipe: Recipe):
    return recipes_db.create(recipe)


@router.put("/recipes/{recipe_uid}", response_model=Recipe, dependencies=[authenticated_account])
def update_recipe(recipe_uid: str, recipe: Recipe):
    return recipes_db.update(recipe_uid, recipe)


@router.delete("/recipes/{recipe_uid}", response_model=Recipe, dependencies=[authenticated_account])
def delete_recipe(recipe_uid: str):
    return recipes_db.delete(recipe_uid)
