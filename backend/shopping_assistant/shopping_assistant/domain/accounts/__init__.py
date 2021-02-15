from typing import List
from fastapi import APIRouter

from shopping_assistant.dependencies import authenticated_account
from shopping_assistant.middleware.plugins import auth

from .schemas import Account, AccountWithPassword
from .database import AccountsDatabase


router = APIRouter()
accounts_db = AccountsDatabase()


@router.get("/accounts/me", response_model=Account)
def get_account_from_token(current_account=authenticated_account):
    return current_account


@router.get("/accounts/{account_uid}", response_model=Account, dependencies=[authenticated_account])
def get_account(account_uid: str):
    return accounts_db.get(account_uid)


@router.get("/accounts", response_model=List[Account], dependencies=[authenticated_account])
def search_accounts():
    return accounts_db.search()


@router.post("/accounts", response_model=Account)
def create_account(account: AccountWithPassword):
    account.password = auth.hash_password(account.password)
    return accounts_db.create(account)


@router.put("/accounts/{account_uid}", response_model=Account, dependencies=[authenticated_account])
def update_account(account_uid: str, account: Account):
    return accounts_db.update(account_uid, account)


@router.delete("/accounts/{account_uid}", response_model=Account, dependencies=[authenticated_account])
def delete_account(account_uid: str):
    return accounts_db.delete(account_uid)
