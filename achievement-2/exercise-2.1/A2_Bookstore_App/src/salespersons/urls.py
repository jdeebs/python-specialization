from django.urls import path
from .views import salespersons

app_name = 'salespersons'

urlpatterns = [
    path('', salespersons),
]