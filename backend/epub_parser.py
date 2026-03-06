import ebooklib
from ebooklib import epub


def parse_upload(file_path):
    book = epub.read_epub(file_path)

    title_meta = book.get_metadata("DC", "title")
    title = title_meta[0][0] if title_meta else "Unkown Title"

    author_meta = book.get_metadata("DC", "creator")
    if len(author_meta) == 1:
        author = author_meta[0][0]
    elif len(author_meta) > 1:
        author = ", ".join([a[0] for a in author_meta])
    else:
        author = "Unkown Author"

    """
    TODO: Finish this function
    - Loop through chapters and store order and name
    - return title, author, and all chapters in dict
    """
