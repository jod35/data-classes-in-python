from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass(frozen=True)
class Book:
    title: str = "title"
    author: str = "author"
    date_published: datetime = datetime(2022, 1, 2)
    num_pages: int = 0


new_book = Book()


print(asdict(new_book))
