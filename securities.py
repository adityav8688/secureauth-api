from passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    print("password length: ", len(password.encode("utf-8")))
    sha_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return pwd_context.hash(sha_hash)

def verify_password(plain: str, hashed: str) -> bool:
    sha_hash = hashlib.sha256(plain.encode("utf-8")).hexdigest()
    return pwd_context.verify(sha_hash, hashed)