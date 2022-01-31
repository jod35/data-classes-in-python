from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass
class Book:
    title: str
    author: str
    date_published: str
    num_pages: int


new_book = Book(
    title="Boojk",
    author="Ssali JOnathan",
    date_published=datetime(2022, 1, 31),
    num_pages=0,
)


print(asdict(new_book))
