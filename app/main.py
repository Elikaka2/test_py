from fastapi import FastAPI
from app.controllers import user_controller, task_controller, cats_controller
from app.database import engine
from app.models import Base

# Создание всех таблиц в БД (если их нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Test FastAPI Project",
    description="Test",
    version="1.0.0"
)

# Подключение роутеров
app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(task_controller.router, prefix="/tasks", tags=["Tasks"])
app.include_router(cats_controller.router, prefix="/cats", tags=["Cats"])

# Простой корневой эндпоинт
@app.get("/")
def root():
    return {"message": "Test"}
