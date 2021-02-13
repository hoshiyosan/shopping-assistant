from typing import List
from shopping_assistant.middleware.schemas import MongoModel, BaseModel


class IngredientQuantity(BaseModel):
    ingredient: str
    quantity: float = None
    unit: str = None


class RecipeSummary(MongoModel):
    name: str
    diners: float


class Recipe(MongoModel):
    name: str
    diners: float
    ingredients: List[IngredientQuantity] = []
    steps: List[str] = []

