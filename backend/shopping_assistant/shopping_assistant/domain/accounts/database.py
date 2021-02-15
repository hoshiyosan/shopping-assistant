from shopping_assistant.middleware.database import Database

class AccountsDatabase(Database):
    def __init__(self):
        super().__init__("accounts")
        self.collection.create_index("email", unique=True)
