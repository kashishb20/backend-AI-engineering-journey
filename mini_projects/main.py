from fastapi import FastAPI, HTTPException
from .database import get_db_connection
from .models import create_table
from .schemas import Task

app = FastAPI()

# Create table on startup
create_table()

# ---------------- ROUTES ----------------

@app.post("/tasks/")
def create_task(task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO tasks (title, description) VALUES (?, ?)",
        (task.title, task.description)
    )
    
    conn.commit()
    conn.close()
    
    return {"message": "Task created successfully"}


@app.get("/tasks/")
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    
    return [dict(task) for task in tasks]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_db_connection()
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()
    conn.close()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return dict(task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    result = conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}