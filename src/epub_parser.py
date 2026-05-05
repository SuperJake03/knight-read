import ebooklib
from ebooklib import epub

from book import Book


# Delete this function
def old_parse_upload(file_path):
    book = epub.read_epub(file_path)

    title_meta = book.get_metadata("DC", "title")
    title = title_meta[0][0] if title_meta else "Unknown Title"

    author_meta = book.get_metadata("DC", "creator")
    if len(author_meta) == 1:
        author = author_meta[0][0]
    elif len(author_meta) > 1:
        author = ", ".join([a[0] for a in author_meta])
    else:
        author = "Unknown Author"

    chapters = []
    index = 0
    for chapter in book.spine:
        item_id = chapter[0]
        item = book.get_item_with_id(item_id)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append({index: item.get_name()})
            index += 1

    return {"title": title, "author": author, "chapters": chapters}


def test_book_content(new_book_obj):
    print(f"Title: {new_book_obj.title}")
    print(f"Author: {new_book_obj.author}")
    print(f"Publisher: {new_book_obj.publisher}")
    print(f"Publication Date: {new_book_obj.pub_date}")
    print(f"Description: {new_book_obj.description}")
    print(f"Subjects: {new_book_obj.subjects}")


def book_upload(file_path):
    book = epub.read_epub(file_path)
    new_book_obj = Book()

    new_book_obj.title = extract_metadata(book.get_metadata("DC", "title"))
    extract_metadata_list(new_book_obj.author, book.get_metadata("DC", "creator"))
    new_book_obj.publisher = extract_metadata(book.get_metadata("DC", "publisher"))
    new_book_obj.pub_date = extract_metadata(book.get_metadata("DC", "date"))
    new_book_obj.description = extract_metadata(book.get_metadata("DC", "description"))
    extract_metadata_list(new_book_obj.subjects, book.get_metadata("DC", "subject"))

    test_book_content(new_book_obj)


def extract_metadata(metadata):
    return metadata[0][0] if metadata else ""


def extract_metadata_list(list, raw):
    for item in raw:
        list.append(item[0])
