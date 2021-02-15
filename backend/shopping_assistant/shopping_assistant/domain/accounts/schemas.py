from shopping_assistant.middleware.schemas import MongoModel

class AccountWithPassword(MongoModel):
    email: str
    password: str

class Account(MongoModel):    
    email: str
