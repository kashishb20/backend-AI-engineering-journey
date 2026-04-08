"""
basically this project is not about tasks .
it represents that i can build a system that
stores , retrieves and manages data
IT ALLOWS US TO :-
-> create task
-> view all and specific task
-> delete task
"""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .database import SessionLocal, engine
from . import models, schemas, crud
from .utils import verify_password

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# 🔐 AUTH ROUTES
# =========================

# ✅ SIGNUP
@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check if user already exists
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    crud.create_user(db, user.email, user.password)

    return {"message": "User created successfully"}


# ✅ LOGIN
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db, user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return {"message": "Login successful"}


# =========================
# 📋 TASK ROUTES
# =========================

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


# ✅ UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status

    db.commit()
    db.refresh(task)

    return task


# ✅ DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}