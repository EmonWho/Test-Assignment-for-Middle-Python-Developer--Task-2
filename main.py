# app/main.py
from fastapi import FastAPI

app = FastAPI()

# Include routers
from .routes import books, authors, clients

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(authors.router, prefix="/authors", tags=["authors"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
