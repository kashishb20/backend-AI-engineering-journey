"""
defines input format and 
used in POST API 
"""
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str
    status: str

class TaskResponse(TaskCreate):
    id: int

    class Config:
        from_attributes = True