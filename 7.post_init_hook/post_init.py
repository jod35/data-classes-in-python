from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Book:
    title: str = "Book"
    author: str = "Ssali Jonathan"
    date_published: datetime = datetime(2022, 12, 22)
    num_pages: int = 0
    author_fullname: str = field(init=False, repr=False)

    def __post_init__(self):
        self.author_fullname = self.author + " " + self.title


new_book = Book()

print(new_book)
print(new_book.author_fullname)
