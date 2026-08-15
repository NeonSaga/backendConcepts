from fastapi import FastAPI
from app.schemas.todo import Todo, TodoCreate, TodoUpdate
from app.routes.todos import router
from app.services.todo_service import todos, next_id
app = FastAPI()

app.include_router(router)










   