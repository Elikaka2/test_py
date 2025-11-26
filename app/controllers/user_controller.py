from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import create_user
from app.database import get_db

router = APIRouter()

@router.post("/create", response_model=UserRead)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserRead).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db, user.username, user.password)
