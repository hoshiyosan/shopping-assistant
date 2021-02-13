from shopping_assistant.middleware.database import Database

class RecipesDatabase(Database):
    def __init__(self):
        super().__init__("recipes")
