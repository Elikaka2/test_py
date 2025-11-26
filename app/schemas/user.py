from pydantic import BaseModel, Field

# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

# Схема для ответа пользователю (без пароля)
class UserRead(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True  # Для Pydantic v1 и Python <3.10
