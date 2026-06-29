from passlib.context import CryptContext
from jose import jwt

SECRET_KEY = "mysecretkey123"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password):

    return pwd_context.hash(
        password
    )

def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

def create_token(username):

    return jwt.encode(
        {"sub": username},
        SECRET_KEY,
        algorithm="HS256"
    )