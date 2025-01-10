from django.shortcuts import render
# Protect function-based views
from django.contrib.auth.decorators import login_required
from .forms import SalesSearchForm

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

# Keep protected
@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)

    # check if the button is clicked
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        print(book_title, chart_type)
        # pack up data to be sent to template via context dictionary
    context = {
        'form': form,
    }
    return render(request, 'sales/records.html', context)