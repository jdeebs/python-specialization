from django.shortcuts import render

# Create your views here.
def salespersons(request):
    return render(request, 'salespersons/salespersons.html')