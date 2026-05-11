from dataclasses import dataclass, field

from ebooklib.epub import Link

type TocEntry = Link | tuple[TocEntry, ...]


@dataclass
class Chapter:
    id: str = ""
    href: str = ""
    title: str = ""
    content: str = ""


@dataclass
class Book:
    # Metadata
    title: str = ""
    author: list[str] = field(default_factory=list)
    publisher: str | None = None
    pub_date: str | None = None
    description: str | None = None
    subjects: list[str] = field(default_factory=list)

    # Structure
    toc: tuple[TocEntry, ...] = ()
    spine: list[tuple[str, str]] = field(default_factory=list)

    # Content
    chapters: list[Chapter] = field(default_factory=list)
