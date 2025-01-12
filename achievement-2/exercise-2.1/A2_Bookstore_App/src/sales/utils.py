from books.models import Book

def get_bookname_from_id(val):
    bookname = Book.objects.get(id=val)
    return bookname