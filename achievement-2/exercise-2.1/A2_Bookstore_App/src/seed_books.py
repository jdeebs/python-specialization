# Run the following commands to add books to the database:
# ** Make sure you're in the project src folder **
# python manage.py shell
# exec(open('seed_books.py').read())

from books.models import Book

books = [
    # Example book input format:
    # "pic" attribute is omitted to be uploaded manually,
    # defaults to the no_picture.jpg file
    # {
    #     "name": "Pride and Prejudice",
    #     "author_name": "Jane Austen",
    #     "genre": "classic",
    #     "book_type": "hardcover",
    #     "price": 12.99,
    # },
    # {
    #     "name": "The Notebook",
    #     "author_name": "Nicholas Sparks",
    #     "genre": "romantic",
    #     "book_type": "ebook",
    #     "price": 8.99,
    # },
]

for book_data in books:
    Book.objects.create(**book_data)
