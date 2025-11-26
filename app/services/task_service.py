from sqlalchemy.orm import Session
from typing import Optional
from app.models.task import Task

def create_task(db: Session, title: str, description: Optional[str]) -> Task:
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_by_status(db: Session, is_done: bool) -> list:
    return db.query(Task).filter(Task.is_done == is_done).all()

def change_task_status(db: Session, task_id: int) -> Optional[Task]:
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.is_done = not task.is_done
        db.commit()
        db.refresh(task)
    return task
