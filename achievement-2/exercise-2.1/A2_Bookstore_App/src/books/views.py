from django.shortcuts import render
# Import to display lists
from django.views.generic import ListView

from .models import Book

# Create your views here.
# Class Based View
class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'