from django.shortcuts import render
# Import to display lists and details
from django.views.generic import ListView, DetailView

from .models import Book

# Create your views here.
# Class Based View
class BookListView(ListView):
    model = Book
    template_name = 'books/books.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'