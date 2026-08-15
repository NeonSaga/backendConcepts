from fastapi import APIRouter
from app.schemas.todo import Todo  , TodoCreate , TodoUpdate
from app.services.todo_service import todos, create_todo, get_todo, patch_todo, delete_todo

router =  APIRouter()



@router.get("/api/todo/{todo_id}")
def get_todo_route(todo_id: int):
        return get_todo(todo_id)


@router.get("/api/todo")
def get_all_todos():
    return todos

@router.post("/api/todo")
def create_todo_route(todo: TodoCreate):
    return  create_todo(todo)

@router.patch("/api/todo/{todo_id}")
def update_todo_route(todo_id: int, updated_todo: TodoUpdate):

    return patch_todo (todo_id ,updated_todo)


@router.delete("/api/todo/{todo_id}")
def delete_todo_route(todo_id: int):
    delete_todo(todo_id)
    