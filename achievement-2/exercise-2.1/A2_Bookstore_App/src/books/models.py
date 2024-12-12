from django.db import models

# Create your models here.
genre_choices = (
        ('classic',
         'Classic'),
        ('romantic',
         'Romantic'),
        ('comic',
         'Comic'),
        ('fantasy',
         'Fantasy'),
        ('horror',
         'Horror'),
        ('educational',
         'Educational'),
    )
book_type_choices = (
        ('hardcover', 'Hardcover'),
        ('ebook', 'E-Book'),
        ('audiob', 'Audiobook'),
)
class Book(models.Model):
    name = models.CharField(max_length=120)
    author_name = models.CharField(max_length=120)
    # List shown as dropdown to user, default value as 'classic'
    genre = models.CharField(max_length=12, 
    choices=genre_choices, default='classic')
    # List shown as dropdown to user, default value as 'hardcover'
    book_type = models.CharField(max_length=12, choices=book_type_choices, default='hardcover')
    # Add tooltip below form field in admin panel
    price = models.FloatField(help_text='in US dollars $')
    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    # Show Book name as string representation when queried
    def __str__(self):
        return str(self.name)