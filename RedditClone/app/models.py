from datetime import datetime
from pydantic import BaseModel

class RedditPost(BaseModel):
    content: str

