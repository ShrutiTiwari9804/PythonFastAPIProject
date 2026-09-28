# import requests
#
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
#
#
# data = response.json()
# print(data[:4])


from fastapi import FastAPI
import requests

app = FastAPI()

# GET ALL DATA

@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()