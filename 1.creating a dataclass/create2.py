from dataclasses import dataclass
from datetime import datetime


@dataclass
class Book:
    title: str
    author: str
    date_published: str
    num_pages: int


new_book1 = Book(
    title="Django For Beginners",
    author="W.S Vicent",
    date_published=datetime(2018, 2, 12),
)

new_book2 = Book(
    title="Django For APIs",
    author="W.S Vicent",
    date_published=datetime(2018, 12, 12),
)

print(new_book1)
print(new_book2)
