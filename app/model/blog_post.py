from pydantic import BaseModel, Field

class BlogPost(BaseModel):
    id: int
    author: str = Field(..., min_length=2, max_length=256)
    title: str = Field(..., min_length=2, max_length=200)
    content: str = Field(..., min_length=1)

    class Config:
        orm_mode = True
