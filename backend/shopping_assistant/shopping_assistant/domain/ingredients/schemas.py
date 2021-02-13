from shopping_assistant.middleware.schemas import MongoModel

class Ingredient(MongoModel):    
    name: str
    unit: str = None
    category: str
