from django.db import models
# Import for username attribute
from django.contrib.auth.models import User

# Create your models here.
class Salesperson(models.Model):
    # OneToOne specifies each username can only be connected to one salesperson
    # CASCADE deletes complete profile of salesperson when username is deleted
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=120)
    bio = models.TextField(default="no bio...")

    pic = models.ImageField(upload_to='salespersons', default='no_picture.jpg')

    # Show salesperson username as string representation when queried
    def __str__(self):
        return str(self.username)