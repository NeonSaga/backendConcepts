from fastapi import FastAPI
from app.schemas.todo import Todo, TodoCreate

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
def update_todo(todo_id: int):
    return{"message": f"Update todo {todo_id}"}


@app.delete("/api/todo/{todo_id}")
def delete_todo(todo_id: int):
    return {"message": f"Delete todo {todo_id}"}