from shopping_assistant.middleware.schemas import MongoModel

class Account(MongoModel):
    first_name: str
    last_name: str 
    email: str

class AccountWithPassword(Account):
    password: str
