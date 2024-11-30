from django.contrib import admin
# Import Book class
from .models import Book

# Register your models here.
admin.site.register(Book)