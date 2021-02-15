from fastapi import Depends
from fastapi.security import HTTPBearer
from shopping_assistant.middleware.plugins import auth
from shopping_assistant.domain.accounts.schemas import Account
from shopping_assistant.domain.accounts.database import AccountsDatabase

accounts_db = AccountsDatabase()
security = HTTPBearer()

class AuthenticatedAccount:
    def __new__(self, authorization: HTTPBearer = Depends(security)):
        token = authorization.credentials
        decoded_token = auth.decode_token(token)
        account = accounts_db.get_by_uid(decoded_token["account_uid"])
        return Account(**account)

authenticated_account = Depends(AuthenticatedAccount)
