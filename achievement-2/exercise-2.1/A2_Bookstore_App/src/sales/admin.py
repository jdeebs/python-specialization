from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    readonly_fields = ('date_created',)
    list_display = ('id', 'book', 'quantity', 'price')
