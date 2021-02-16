import re
from typing import List
from fastapi import APIRouter
from shopping_assistant.dependencies import authenticated_account

from .schemas import ShoppingList, ShoppingListSummary
from .database import ShoppingListsDatabase


router = APIRouter()
shoppinglists_db = ShoppingListsDatabase()


@router.get("/shoppinglists/{shoppinglist_uid}", response_model=ShoppingList, dependencies=[authenticated_account])
def get_shoppinglist(shoppinglist_uid: str):
    return shoppinglists_db.get_by_uid(shoppinglist_uid)


@router.get("/shoppinglists", response_model=List[ShoppingListSummary], dependencies=[authenticated_account])
def search_shoppinglists(query:str=""):
    return shoppinglists_db.search({
        "name": {"$regex": re.compile(query, re.IGNORECASE)}
    })


@router.post("/shoppinglists", response_model=ShoppingList, dependencies=[authenticated_account])
def create_shoppinglist(shoppinglist: ShoppingList):
    return shoppinglists_db.create(shoppinglist)


@router.put("/shoppinglists/{shoppinglist_uid}", response_model=ShoppingList, dependencies=[authenticated_account])
def update_shoppinglist(shoppinglist_uid: str, shoppinglist: ShoppingList):
    return shoppinglists_db.update(shoppinglist_uid, shoppinglist)


@router.delete("/shoppinglists/{shoppinglist_uid}", response_model=ShoppingList, dependencies=[authenticated_account])
def delete_shoppinglist(shoppinglist_uid: str):
    return shoppinglists_db.delete(shoppinglist_uid)
