from shopping_assistant.middleware.database import Database

class IngredientsDatabase(Database):
    def __init__(self):
        super().__init__("ingredients")
        self.collection.create_index("name", unique=True)
