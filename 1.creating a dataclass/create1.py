from datetime import datetime


class Book:
    def __init__(self, title, author, date_published, num_pages):
        self.title = title
        self.author = author
        self.date_published = date_published
        self.num_pages = num_pages


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
