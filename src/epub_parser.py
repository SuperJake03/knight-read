import ebooklib
from book import Book
from bs4 import BeautifulSoup
from ebooklib import epub


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
    print(f"Table of Contents: {new_book_obj.toc}")
    print(f"Spine: {new_book_obj.spine}")
    print("")


def book_upload(file_path):
    book = epub.read_epub(file_path)
    new_book_obj = Book()

    extract_metadata(book, new_book_obj)
    extract_chapters(book, new_book_obj)
    test_book_content(new_book_obj)


def extract_metadata(book, new_book_obj):
    new_book_obj.title = metadata_helper(book.get_metadata("DC", "title"))
    metadata_list_helper(new_book_obj.author, book.get_metadata("DC", "creator"))
    new_book_obj.publisher = metadata_helper(book.get_metadata("DC", "publisher"))
    new_book_obj.pub_date = metadata_helper(book.get_metadata("DC", "date"))
    new_book_obj.description = metadata_helper(book.get_metadata("DC", "description"))
    metadata_list_helper(new_book_obj.subjects, book.get_metadata("DC", "subject"))
    new_book_obj.toc = book.toc
    new_book_obj.spine = book.spine


def metadata_helper(metadata):
    return metadata[0][0] if metadata else ""


def metadata_list_helper(list, raw):
    for item in raw:
        list.append(item[0])


"""
Finish extracting chapters logic
create chapter dataclass
"""


def extract_chapters(book, new_book_obj):
    for item_id, _ in new_book_obj.spine:
        item = book.get_item_with_id(item_id)
        content = item.get_content()
        # soup = BeautifulSoup(content, "html.parser")
        print(content)
        print("\n")
        # print(soup)
