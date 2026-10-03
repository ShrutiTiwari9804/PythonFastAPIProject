from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found"
        )
    return {
        "id": 1,
        "name": "Mohit"
    }
