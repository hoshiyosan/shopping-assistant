from datetime import datetime
from typing import List
from pydantic import Field
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
    created: datetime = Field(default_factory=datetime.now)


class ShoppingList(ShoppingListSummary):
    ingredients: List[IngredientQuantity] = []
    recipes: List[ShoppingListRecipe] = []
