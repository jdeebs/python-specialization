from django.contrib import admin
# Import Customer class
from .models import Customer

# Register your models here.
admin.site.register(Customer)