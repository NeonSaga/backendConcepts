from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    completed: bool = False



class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False 