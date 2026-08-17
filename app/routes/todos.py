from fastapi import APIRouter, Depends
from app.schemas.todo import Todo  , TodoCreate , TodoUpdate
from app.services.todo_service import todos, create_todo, get_todo, patch_todo, delete_todo
from app.database import get_db
from app.models.todo import Todo as TodoModel


router =  APIRouter()


@router.get("/api/todo")
def get_all_todos(db = Depends(get_db)):
    return db.query(TodoModel).all()


@router.get("/api/todo/{todo_id}")
def get_todo_route(todo_id: int):
        return get_todo(todo_id)


@router.post("/api/todo")
def create_todo_route(todo: TodoCreate, db = Depends(get_db)):
    return  create_todo(todo, db)

@router.patch("/api/todo/{todo_id}")
def update_todo_route(todo_id: int, updated_todo: TodoUpdate):

    return patch_todo (todo_id ,updated_todo)


@router.delete("/api/todo/{todo_id}")
def delete_todo_route(todo_id: int):
    delete_todo(todo_id)
    