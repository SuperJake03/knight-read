import os

from backend.epub_parser import parse_upload
from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

books = {}

"""
TODO:
    Finish endpoints
    - Get a books chapters
    - Get a books chapter content
"""


@app.get("/books")
def get_all_books():
    return books


@app.get(f"/books/{id}")
def get_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Item not found")
    return books[id]


@app.post("/books")
def upload_book(file: UploadFile = File(..., description="Book file as UploadFile")):
    file_name = os.path.basename(file.filename)
    file_path = os.path.join("books", file_name)

    content = file.file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    book_data = parse_upload(file_path)
    id = max(books.keys(), default=0) + 1
    books[id] = {
        "title": book_data["title"],
        "author": book_data["author"],
        "file_name": file_name,
        "chapters": book_data["chapters"],
    }
    return {
        "id": id,
        "title": book_data["title"],
        "author": book_data["author"],
        "file_name": file_name,
        "chapter_count": len(book_data["chapters"]),
    }
