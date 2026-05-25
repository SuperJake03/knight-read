import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub

from book import Book, Chapter


def test_book_content(new_book_obj):
    print(f"Title: {new_book_obj.title}")
    print(f"Author: {new_book_obj.author}")
    print(f"Publisher: {new_book_obj.publisher}")
    print(f"Publication Date: {new_book_obj.pub_date}")
    print(f"Description: {new_book_obj.description}")
    print(f"Subjects: {new_book_obj.subjects}")
    print(f"Table of Contents: {new_book_obj.toc}")
    print(f"Spine: {new_book_obj.spine}")
    print(f"Num of Chapters: {len(new_book_obj.chapters)}")
    print("")


def book_upload(file_path):
    book = epub.read_epub(file_path)

    title = metadata_helper(book.get_metadata("DC", "title"))
    author = metadata_list_helper([], book.get_metadata("DC", "creator"))
    publisher = metadata_helper(book.get_metadata("DC", "publisher"))
    pub_date = metadata_helper(book.get_metadata("DC", "date"))
    description = metadata_helper(book.get_metadata("DC", "description"))
    subjects = metadata_list_helper([], book.get_metadata("DC", "subject"))
    toc = book.toc
    spine = book.spine

    new_book_obj = Book(
        title=title,
        author=author,
        publisher=publisher,
        pub_date=pub_date,
        description=description,
        subjects=subjects,
        toc=toc,
        spine=spine,
        chapters=[],
    )

    extract_chapters(book, new_book_obj)
    # test_book_content(new_book_obj)
    return new_book_obj


def metadata_helper(metadata):
    return metadata[0][0] if metadata else ""


def metadata_list_helper(list, raw):
    for item in raw:
        list.append(item[0])


def extract_chapters(book, new_book_obj):
    for item_id, _ in new_book_obj.spine:
        item = book.get_item_with_id(item_id)
        if item.is_chapter():
            body = item.get_body_content()
            soup = BeautifulSoup(body, "html.parser")
            href = item.get_name()
            title_tag = soup.find("h1")
            title = title_tag.get_text() if title_tag else "Chapter Title N/A"
            content = soup.get_text().strip()
            new_chap_obj = Chapter(id=item_id, href=href, title=title, content=content)
            new_book_obj.chapters.append(new_chap_obj)


# def get_title(toc, tgt_href):
#     for toc_item in toc:
#         title = get_title_helper(toc_item, tgt_href)
#         if title:
#             return title
#     return "Not found"


# def get_title_helper(toc_item, tgt_href):
#     if isinstance(toc_item, epub.Link):
#         href_trimmed = toc_item.href.split("#")[0]
#         if href_trimmed.endswith(tgt_href):
#             print(toc_item.title)
#             return toc_item.title
#     elif isinstance(toc_item, tuple):
#         for item in toc_item:
#             title = get_title_helper(item, tgt_href)
#             if title:
#                 return title
