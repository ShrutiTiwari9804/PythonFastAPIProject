from fastapi import FastAPI, HTTPException , File, UploadFile, Form, Depends
from schemas import PostCreate, PostResponse
from db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select

from imagekitio import ImageKit


import shutil
import uuid
import tempfile
import os

from dotenv import load_dotenv

load_dotenv()

imagekit = ImageKit (
    private_key = os.getenv("IMAGEKIT_PRIVATE_KEY")
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    

app = FastAPI(lifespan=lifespan)

# text_posts = {
#     1: {"title": "Morning Routine", "content": "Starting the day with a fresh mind and a clear plan."},
#     2: {"title": "Python Tip", "content": "Break a big problem into smaller functions and solve them one step at a time."},
#     3: {"title": "Learning Journey", "content": "Learning something new every day may feel slow, but consistency creates progress."},
#     4: {"title": "Backend Development", "content": "APIs connect different parts of an application and allow them to communicate with each other."},
#     5: {"title": "Debugging", "content": "A bug is not always a mistake; sometimes it is simply a clue that helps you understand the code better."},
#     6: {"title": "Tech Insight", "content": "Writing clean and simple code makes it easier to test, maintain, and improve later."},
#     7: {"title": "Study Motivation", "content": "You do not have to understand everything in one day. Keep learning and revisit difficult topics."},
#     8: {"title": "Weekend Plans", "content": "Planning to work on a small coding project and learn something interesting this weekend."},
#     9: {"title": "Question", "content": "What is one programming concept that took you a long time to understand?"},
#     10: {"title": "Project Update", "content": "Just finished adding a new feature to my project. Now it is time to test everything."},
#     11: {"title": "FastAPI", "content": "FastAPI makes it simple to create APIs using Python with automatic documentation and validation."},
#     12: {"title": "Developer Life", "content": "Some days you write a lot of code, and some days you spend hours fixing one small error."},
#     13: {"title": "Learning From Errors", "content": "Reading error messages carefully can often tell you exactly where the problem is."},
#     14: {"title": "Database Tip", "content": "Good database design can make an application easier to manage as the project grows."},
#     15: {"title": "Small Achievement", "content": "Finally understood a concept that was confusing yesterday. Small progress is still progress."},
# }

# @app.get("/posts")
# def get_all_posts(limit: int = None)-> PostResponse:
#     if limit:
#         return list(text_posts.values())[:limit]

#     return text_posts

# @app.get("/posts/{id}")
# def get_post(id:int)-> PostResponse:
#     if id not in text_posts:
#         raise HTTPException (status_code=404,detail= "Post Not Found")
#     return text_posts.get(id)


# @app.post("/posts")
# def create_post(post : PostCreate) -> PostResponse:
#     new_post =  {"title": post.title, "content": post.content}
#     text_posts[max(text_posts.keys()) + 1] = new_post
#     return new_post


@app.post("/uploads")
async def upload_file(
    file: UploadFile = File (...),
    caption : str = Form(""),
    session : AsyncSession = Depends(get_async_session)
):

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False, 
            suffix=os.path.splitext(file.filename)[1]
            ) as temp_file:

            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        with open (temp_file_path, "rb") as file_data:

            upload_result = imagekit.files.upload (
                file = file_data,
                file_name = file.filename
            )
        

       

            post = Post( 
                caption = caption,
                url = upload_result.url,
                file_type = "video" if file.content_type.startswith("video/") else "image",
                file_name = upload_result.name
            )

            session.add(post)
            await session.commit()
            await session.refresh(post)
            return post 
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()


@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends (get_async_session)

):

    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type" : post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }
        )

    return {"posts": posts_data}



 