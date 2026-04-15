from passlib.context import CryptContext
# import bcrypt
# import hashlib

# bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    # pre_hashed = hashlib.sha256(password.encode()).hexdigest()
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # pre_hashed = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(plain_password, hashed_password)



