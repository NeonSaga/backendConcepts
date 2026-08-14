from fastapi import FastAPI
from app.schemas.todo import Todo, TodoCreate, TodoUpdate

app = FastAPI()

todos = []
next_id = 1 

@app.get("/api/todo/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo 
    return {"message": "Todo not found"}


@app.post("/api/todo")
def create_todo(todo: TodoCreate):
    global next_id

    new_Todo= Todo(
        id = next_id,
        title = todo.title,
        completed = todo.completed
    )
    todos.append(new_Todo)

    next_id += 1
    return new_Todo


@app.patch("/api/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoUpdate):

    for todo in todos:
        if todo.id == todo_id:

            if updated_todo.title is not None:
                todo.title = updated_todo.title

            if updated_todo.completed is not None:
                todo.completed = updated_todo.completed

            return todo
    return{"message": "Todo not found"}


@app.delete("/api/todo/{todo_id}")
def delete_todo(todo_id: int):
    return {"message": f"Delete todo {todo_id}"}