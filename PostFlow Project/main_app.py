from fastapi import FastAPI, HTTPException


app = FastAPI()

text_posts = {
    1: {"title": "Morning Routine", "content": "Starting the day with a fresh mind and a clear plan."},
    2: {"title": "Python Tip", "content": "Break a big problem into smaller functions and solve them one step at a time."},
    3: {"title": "Learning Journey", "content": "Learning something new every day may feel slow, but consistency creates progress."},
    4: {"title": "Backend Development", "content": "APIs connect different parts of an application and allow them to communicate with each other."},
    5: {"title": "Debugging", "content": "A bug is not always a mistake; sometimes it is simply a clue that helps you understand the code better."},
    6: {"title": "Tech Insight", "content": "Writing clean and simple code makes it easier to test, maintain, and improve later."},
    7: {"title": "Study Motivation", "content": "You do not have to understand everything in one day. Keep learning and revisit difficult topics."},
    8: {"title": "Weekend Plans", "content": "Planning to work on a small coding project and learn something interesting this weekend."},
    9: {"title": "Question", "content": "What is one programming concept that took you a long time to understand?"},
    10: {"title": "Project Update", "content": "Just finished adding a new feature to my project. Now it is time to test everything."},
    11: {"title": "FastAPI", "content": "FastAPI makes it simple to create APIs using Python with automatic documentation and validation."},
    12: {"title": "Developer Life", "content": "Some days you write a lot of code, and some days you spend hours fixing one small error."},
    13: {"title": "Learning From Errors", "content": "Reading error messages carefully can often tell you exactly where the problem is."},
    14: {"title": "Database Tip", "content": "Good database design can make an application easier to manage as the project grows."},
    15: {"title": "Small Achievement", "content": "Finally understood a concept that was confusing yesterday. Small progress is still progress."},
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]

    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    if id not in text_posts:
        raise HTTPException (status_code=404,detail= "Post Not Found")
    return text_posts.get(id)


