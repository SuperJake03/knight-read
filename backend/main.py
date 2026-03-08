import os

from backend.epub_parser import parse_upload
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

id_count = 0
books = {}


@app.post("/books")
def upload_book(file: UploadFile = File(..., description="Book file as UploadFile")):
    file_name = os.path.basename(file.filename)
    file_path = os.path.join("books", file_name)

    content = file.file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    # call epub parser on f"books/{file_name}" to retrieve ID, Title, Author, Chapters, Cover Page
    metadata = parse_upload(file_path)
    # append new book to the books dict with new id
    # return new book metadata
    return {
        "TODO": "Return the books ID, Title, Author, Chapters, Cover Page, file_name"
    }
