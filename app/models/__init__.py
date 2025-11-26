from sqlalchemy.ext.declarative import declarative_base

# Общий Base для всех моделей
Base = declarative_base()

# Импорт моделей для удобного доступа
from app.models.user import User
from app.models.task import Task
