from dataclasses import dataclass, field

from ebooklib.epub import Link


@dataclass
class Chapter:
    pass


@dataclass
class Image:
    pass


@dataclass
class StyleSheet:
    pass


@dataclass
class Book:
    # Metadata
    title: str = ""
    author: list[str] = field(default_factory=list)
    identifier: str = ""
    publisher: str | None = ""
    pub_date: str | None = ""
    description: str | None = ""
    subjects: list[str] = field(default_factory=list)

    # # Structure
    type TocEntry = Link | tuple[TocEntry, ...]
    toc: tuple[TocEntry, ...] = ()
    spine: list[tuple[str, str]] = field(default_factory=list)

    # # Content
    # chapters: list[Chapter] = field(default_factory=list)
    # images: list[Image] = field(default_factory=list)
    # style_sheets: list[StyleSheet] = field(default_factory=list)
