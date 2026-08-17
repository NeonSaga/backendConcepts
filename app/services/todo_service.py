from app.schemas.todo import Todo, TodoUpdate , TodoCreate
from app.models.todo import Todo as TodoModel
from sqlalchemy.orm import Session 


todos = []
next_id = 1 


def get_todo(todo_id):
    for todo in todos:
        if todo.id == todo_id:
            return todo 
        
    return {"message": "Todo not found"}



def create_todo(todo, db: Session):
    global next_id

    new_todo = TodoModel(
        title = todo.title,
        completed = todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo

def patch_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in todos:
            if todo.id == todo_id:
    
                if updated_todo.title is not None:
                    todo.title = updated_todo.title
    
                if updated_todo.completed is not None:
                    todo.completed = updated_todo.completed
    
                return todo
            
    return{"message": "Todo not found"}





def delete_todo(todo_id):
    for todo in todos:
            if todo.id == todo_id:
                todos.remove(todo) 
                return {"message": "Todo Deleted"}
    
    return{"message": "Todo not found"} 