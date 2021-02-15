from typing import List
from shopping_assistant.middleware.schemas import MongoModel, BaseModel


class IngredientQuantity(BaseModel):
    ingredient: str
    quantity: float = None
    unit: str = None


class RecipeSummary(MongoModel):
    name: str
    diners: float
    thumbnail: str = None


class Recipe(RecipeSummary):
    ingredients: List[IngredientQuantity] = []
    steps: List[str] = []
