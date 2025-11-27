from sqlalchemy.orm import Session
from app.models.user import User
import bcrypt

def create_user(db: Session, username: str, password: str) -> User:
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username=username, password_hash=password_hash)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
