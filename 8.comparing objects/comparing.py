from dataclasses import dataclass, field
from datetime import datetime


@dataclass(order=True)
class Book:
    title: str = "Book"
    author: str = "Ssali JOnathan"
    date_published: datetime = datetime(2022, 12, 1)
    num_pages: int = 0
    sort_index: int = field(init=False, repr=False)

    def __post_init__(self):
        self.sort_index = self.num_pages


book1 = Book(num_pages=30)
book2 = Book(num_pages=40)

print(book1 > book2)
