from shopping_assistant.middleware.database import Database

class ShoppingListsDatabase(Database):
    def __init__(self):
        super().__init__("shoppinglists")
