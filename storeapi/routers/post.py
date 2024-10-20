import asyncio

from fastapi import APIRouter, HTTPException

from storeapi.database import comment_table, database, post_table
from storeapi.models.post import (
    Comment,
    CommentIn,
    PostWithComment,
    UserPost,
    UserPostIn,
)

router = APIRouter()


def _factorize():
    for i in range(1, 100_000):
        if i == 9000:
            return i * 1000


async def find_post(post_id: int) -> UserPost:
    query = post_table.select().where(post_table.c.id == post_id)
    return await database.fetch_one(query)


@router.post("/post", response_model=UserPost, status_code=201)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    query = post_table.insert().values(data)
    last_record_id = await database.execute(query)
    new_post = {**data, "id": last_record_id}
    return new_post


@router.get("/post", response_model=list[UserPost])
async def get_all_posts():
    query = post_table.select()
    return await database.fetch_all(query)


@router.post("/comment", response_model=Comment, status_code=201)
async def create_comment(comment: CommentIn):
    post = await find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not exist")
    data = comment.model_dump()
    query = comment_table.insert().values(data)
    last_record_id = await database.execute(query)
    new_comment = {**data, "id": last_record_id}
    return new_comment


@router.get("/post/{post_id}/comment", response_model=list[Comment], status_code=200)
async def get_comments_on_post(post_id: int):
    query = comment_table.select().where(comment_table.c.post_id == post_id)
    return await database.fetch_all(query)


@router.get("/post/{post_id}", response_model=PostWithComment, status_code=200)
async def get_post_with_comments(post_id: int):
    post = await find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"post": post, "comments": await get_comments_on_post(post_id)}


@router.get("/factorize", status_code=200)
async def factorize():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, _factorize)
    return result


@router.get("/health", response_model=dict, status_code=200)
async def health():
    return {"health": "good"}


@router.get("/greetings", response_model=dict, status_code=200)
async def greetings():
    pass
