from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=120)
    notes = models.TextField()
    pic = models.ImageField(upload_to='customers', default='no_picture.jpg')

    # Show customer name as string representation when queried
    def __str__(self):
        return str(self.name)
