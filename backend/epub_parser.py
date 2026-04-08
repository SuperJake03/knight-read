import ebooklib
from ebooklib import epub

"""
Look into changes, using tkinter now
"""


def parse_upload(file_path):
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


"""
TODO:
    - Finish this function, look into BeautifulSoup
"""


def parse_content(file_path, content_name):
    pass
