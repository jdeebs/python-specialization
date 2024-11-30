from django.db import models

# Create your models here.
class Sale(models.Model):
    # Book identifier
    # Use string reference to the Book model to avoid circular import error
    # 'books' is from the name attribute in books apps.py file
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    # Number of books sold
    quantity = models.PositiveIntegerField()
    # Total sale price for the sale
    price = models.FloatField()
    # Date of sale, automatically set to current date
    date_created = models.DateTimeField(auto_now_add=True)