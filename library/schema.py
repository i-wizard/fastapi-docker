from pydantic import BaseModel


class BookSerializer(BaseModel):
    title: str
    rating: int
    author_id: int
    
    class Config:
        orm_mode = True


class AuthorSerializer(BaseModel):
    name: str
    
    class Config:
        orm_mode = True