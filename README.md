Проект на FastAPI с PostgreSQL, SQLAlchemy, Pydantic и интеграцией с внешним API (Cat Facts).  

---

## Структура проекта

app/
controllers/ # Эндпоинты
models/ # SQLAlchemy модели
schemas/ # Валидация
services/ # Бизнес-логика
database.py # Подключение к базе данных
main.py # Точка входа приложения
.venv/ # Виртуальное окружение
requirements.txt # Зависимости

## Установка

1. Клонировать репозиторий:

git clone <YOUR_REPO_URL>
cd <REPO_FOLDER>
Создать и активировать виртуальное окружение:

.venv\Scripts\activate

pip install -r requirements.txt

Настроить PostgreSQL:

Создать базу данных

В app/database.py указать правильный DATABASE_URL:

DATABASE_URL = "postgresql://username:password@localhost:5432/testdb"

## Запуск приложения

uvicorn app.main:app --reload

Swagger UI: http://127.0.0.1:8000/docs

## Эндпоинты
Users

POST /users/create — создать пользователя

Вход: {"username": "testuser", "password": "123456"}

Выход: {"id": 1, "username": "testuser"}

Cats

GET /cats/fact — получить случайный факт о кошках

Выход: {"fact": "Кошки мурлыкают", "is_small_fact": true}

Tasks

POST /tasks/create — создать задачу

Вход: {"title": "Сделать тест", "description": "Проверить FastAPI"}

Выход: {"id":1,"title":"Сделать тест","description":"Проверить FastAPI","is_done":false}

GET /tasks/done — получить готовые задачи

GET /tasks/not-done — получить неготовые задачи

PATCH /tasks/{task_id}/change-status — изменить статус задачи

Выход: JSON с обновлённой задачей

## Особенности
Хэширование пароля пользователей (bcrypt)

Валидация входных данных через Pydantic

Интеграция с внешним API: https://catfact.ninja/fact

Слойная архитектура: модели, сервисы, контроллеры, схемы

## Примечания
Все эндпоинты документированы в Swagger
