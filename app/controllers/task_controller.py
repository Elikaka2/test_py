from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.task import TaskCreate, TaskRead
from app.services.task_service import create_task, get_tasks_by_status, change_task_status
from app.database import get_db

router = APIRouter()

@router.post("/create", response_model=TaskRead)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task.title, task.description)

@router.get("/done", response_model=List[TaskRead])
def get_done_tasks(db: Session = Depends(get_db)):
    return get_tasks_by_status(db, is_done=True)

@router.get("/not-done", response_model=List[TaskRead])
def get_not_done_tasks(db: Session = Depends(get_db)):
    return get_tasks_by_status(db, is_done=False)

@router.patch("/{task_id}/change-status", response_model=TaskRead)
def change_status(task_id: int, db: Session = Depends(get_db)):
    task = change_task_status(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
