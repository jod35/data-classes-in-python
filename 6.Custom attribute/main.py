from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Book:
    title: str = "Book"
    date_published: datetime = datetime(2021, 12, 1)
    num_pages: int = 2
    author: str = field(init=False, repr=False)


new_book = Book()


print(new_book)
