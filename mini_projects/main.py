"""
basically this project is not about tasks .
it represents that i can build a system that
stores , retrieves and manages data
IT ALLOWS US TO :-
-> create task
-> view all and specific task
-> delete task
"""

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import SessionLocal, engine
from . import models, schemas

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS Middleware (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ CREATE TASK
@app.post("/tasks/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# ✅ READ ALL TASKS
@app.get("/tasks/")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


# ✅ DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    
    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()
    return {"message": "Deleted"}


# ✅ UPDATE TASK (NEW - completes CRUD)
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status

    db.commit()
    db.refresh(task)

    return task