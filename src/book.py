from dataclasses import dataclass, field
from typing import Optional


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
    publisher: str = ""
    pub_date: str = ""
    description: str = ""
    subjects: list[str] = field(default_factory=list)

    # Structure
    toc: list[dict] = field(default_factory=list)
    spine: list[str] = field(default_factory=list)

    # Content
    chapters: list[Chapter] = field(default_factory=list)
    images: list[Image] = field(default_factory=list)
    style_sheets: list[StyleSheet] = field(default_factory=list)
