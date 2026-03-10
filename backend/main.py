import os

from backend.epub_parser import parse_upload
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

books = {}


@app.get("/books")
def get_all_books():
    return books


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
