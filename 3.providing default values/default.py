from dataclasses import dataclass
from datetime import datetime
import pprint


@dataclass
class Book:
    author: str
    date_published: str
    num_pages: int
    title: str = "Book"

    def return_info(self):
        return f"<Book {self.title}"


new_book = Book(
    author="Ssali Jonathan", date_published=datetime(2022, 1, 23), num_pages=20
)


print(new_book)
