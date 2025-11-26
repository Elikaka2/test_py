from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.models.user import User

def create_user(db: Session, username: str, password: str) -> User:
    password_hash = bcrypt.hash(password)
    user = User(username=username, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
