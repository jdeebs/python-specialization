from django.db import models
# Import Book class
from .models import Book

# Create your models here.
class Sale(models.Model):
    # Book identifier
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # Number of books sold
    quantity = models.PositiveIntegerField()
    # Total sale price for the sale
    price = models.FloatField()
    # Date of sale, automatically set to current date
    date_created = models.DateTimeField(auto_now_add=True)