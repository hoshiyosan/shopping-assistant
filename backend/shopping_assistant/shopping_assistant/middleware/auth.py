import jwt
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta


class Authentication:
    def __init__(self, *, secret_key, encryption_algorithm="HS256"):
        self.crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.secret_key = secret_key
        self.encryption_algorithm = encryption_algorithm

    def verify_password(self, plain_password, hashed_password):
        return self.crypt_context.verify(plain_password, hashed_password)

    def hash_password(self, plain_password):
        return self.crypt_context.hash(plain_password)

    def generate_access_token(self, token_data: dict, expires_delta: Optional[timedelta] = None):
        token_data = token_data.copy()

        if expires_delta:
            expires = datetime.utcnow() + expires_delta
        else:
            expires = datetime.utcnow() + timedelta(minutes=15)
        
        token_data.update({"exp": expires})
        encoded_jwt = jwt.encode(token_data, self.secret_key, algorithm=self.encryption_algorithm)
        return {"access_token": encoded_jwt, "expires": expires}

    def decode_token(self, token):
        return jwt.decode(token, self.secret_key, algorithms=[self.encryption_algorithm])
