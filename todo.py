from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo (BaseModel):
    id:int
    title:str
    completed:bool

@app.post ("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"TODO added", "data":todo}

@app.get("/todos")
def get_todo():
    return todos

@app.get("/todos/{todo_id")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "todo not found"}

@app.put ("/todos/{todo_id}")
def update_todo(todo:int, updated_todo:Todo, todo_id=None):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {
                "message": "data updated",
                "data": updated_todo
            }
    return {"error": "todo not found"}

@app.delete("/todos/{todo_id")
def delete_todo (todo_id:int):
    for index , todo in enumerate (todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {
                "message": "data deleted"
            }
    return {"error": "todo not found"}


