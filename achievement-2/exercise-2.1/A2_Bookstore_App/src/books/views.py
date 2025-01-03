from django.shortcuts import render
# Import to display lists and details
from django.views.generic import ListView, DetailView
# To protect class-based view
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

# Create your views here.
# Class Based 'protected' View
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/books.html'

# Class Based 'protected' View
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'