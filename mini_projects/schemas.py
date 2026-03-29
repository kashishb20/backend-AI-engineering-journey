"""
defines input format and 
used in POST API 
"""
from pydantic import BaseModel 

class Task(BaseModel):
    title: str 
    description: str
    