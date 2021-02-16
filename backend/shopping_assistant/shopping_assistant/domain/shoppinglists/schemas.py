from typing import List
from shopping_assistant.middleware.schemas import MongoModel, BaseModel


class IngredientQuantity(BaseModel):
    ingredient: str
    quantity: float = None
    unit: str = None


class ShoppingListRecipe(BaseModel):
    uid: str
    name: str
    diners: float
    thumbnail: str = None
    

class ShoppingListSummary(MongoModel):
    name: str


class ShoppingList(ShoppingListSummary):
    ingredients: List[IngredientQuantity] = []
    recipes: List[ShoppingListRecipe] = []
