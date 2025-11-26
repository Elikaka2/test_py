from pydantic import BaseModel, Field
from typing import Optional

# Схема для создания задачи
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)

# Схема для ответа о задаче
class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_done: bool

    class Config:
        orm_mode = True  # Для Pydantic v1 и Python <3.10
