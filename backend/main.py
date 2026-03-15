import os

from backend.epub_parser import parse_content, parse_upload
from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()

books = {}


@app.get("/books")
def get_all_books():
    return books


@app.get("/books/{id}")
def get_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[id]


@app.get("/books/{id}/chapters")
def get_all_chapters(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[id]["chapters"]


"""
TODO: finish
    Finish API endpoints
    - FINISH get_chapter_content epub parser call
"""


@app.get("/books/{id}/chapters/{index}")
def get_chapter_content(id: int, index: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    indexes = set([content["index"] for content in books[id]["chapters"]])
    if index not in indexes:
        raise HTTPException(status_code=404, detail="Content not found")
    content_name = books[id]["chapters"][index]
    file_path = os.path.join("books", books[id]["file_name"])
    chapter_content = parse_content(file_path, content_name)
    return {
        "chapter_index": index,
        "chapter_count": len(books[id]["chapters"]),
        "content": chapter_content,
    }


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
