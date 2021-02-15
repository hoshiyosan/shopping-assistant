from fastapi import APIRouter
from shopping_assistant.middleware.exceptions import AuthenticationError, ObjectNotFound
from shopping_assistant.middleware.plugins import auth
from .schemas import LoginCredentials
from ..accounts import accounts_db

router = APIRouter()

@router.post("/auth/token")
def generate_token(credentials: LoginCredentials):
    try:
        account = accounts_db.get({"email": credentials.email})
    except ObjectNotFound as error:
        raise AuthenticationError(error="Authentication error. Account doesn't exists!") from error
    if not auth.verify_password(credentials.password, account["password"]):
        raise AuthenticationError(error="Authentication error. Password doesn't match!")
    print(account)
    return auth.generate_access_token({"account_uid": str(account["_id"])})
