from fastapi import FastAPI
from .models import RedditPost
from .db import DbStuff


app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Status":"App LIVE"}


@app.post("/new_post", tags=['Post new Post'])
async def CreatePost(new_post:RedditPost) -> dict:
    DbStuff.AddPost(new_post)
    return {"Status":"Post added successfully"}

@app.get("/home", tags=['Get all posts'])
async def FetchAllPosts() -> dict:
    data = DbStuff.FetchAllPosts()
    return {"All_posts":data}

#update post ,delete post ,get post
@app.put("/edit_post/{id}", tags=['Update post'])
async def UpdatePost(id:int, content: dict) -> dict:
    DbStuff.EditPost(id,content)
    return {"Status":"Update successful"}

#@app.post("/add_vote", tags=['Add vote'])
#async def AddVote(vote):
