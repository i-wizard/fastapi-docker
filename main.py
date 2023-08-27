from typing import List

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from library.schema import BookSerializer, AuthorSerializer
from library.models import Book, Author
from settings import settings


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)

@app.get("/")
def root():
    return {"message":"Welcome home"}

@app.post("/books", response_model=BookSerializer, status_code=201)
def add_book(book:BookSerializer):
    data:dict = book.model_dump(mode='json')
    book_data = Book(**data)
    db.session.add(book_data)
    db.session.commit()
    return book_data


@app.post("/authors", response_model=AuthorSerializer, status_code=201)
def add_author(author:AuthorSerializer):
    data:dict = author.model_dump(mode='json')
    author_data = Author(**data)
    db.session.add(author_data)
    db.session.commit()
    return author_data

@app.get("/authors", response_model=List[AuthorSerializer])
def list_authors():
    authors = db.session.query(Author).all()
    return authors