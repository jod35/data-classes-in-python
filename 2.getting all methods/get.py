from dataclasses import dataclass
from datetime import datetime
import pprint


@dataclass
class Book:
    title: str
    author: str
    date_published: str
    num_pages: int

    def return_info(self):
        return f"<Book {self.title}"


pprint.pprint(dir(Book))
