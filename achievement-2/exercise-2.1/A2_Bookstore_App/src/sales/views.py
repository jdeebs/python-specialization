from django.shortcuts import render
# Protect function-based views
from django.contrib.auth.decorators import login_required
# To render the sales search form
from .forms import SalesSearchForm
# To access sales records
from .models import Sale
import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'sales/home.html')

# Keep protected
@login_required
def records(request):
    form = SalesSearchForm(request.POST or None)
    # Init dataframe to None
    sales_df = None

    # check if the button is clicked
    if request.method == 'POST':
        book_title = request.POST.get('book_title')
        chart_type = request.POST.get('chart_type')
        
        qs = Sale.objects.filter(book__name=book_title)
        if qs:
            # Convert queryset values to pandas dataframe
            sales_df = pd.DataFrame(qs.values())
            # Convert DataFrame to readable in html
            sales_df = sales_df.to_html()

        print('Exploring querysets:')
        print('Case 1: Output of Sale.objects.all()')
        qs = Sale.objects.all()
        print(qs)

        # Django's ORM uses double underscore (__) 
        # in querysets to access fields
        # This is to differentiate between
        # operations on the database level rather than
        # the Python object level (dot notation)
        print('Case 2: Output of Sale.objects.filter(book__name=book_title)')
        qs = Sale.objects.filter(book__name=book_title)
        print(qs)

        print('Case 3: Output of qs.values')
        print(qs.values())

        print('Case 4: Output of qs.values_list()')
        print(qs.values_list())

        print('Case 5: Output of Sale.objects.get(id=1)')
        obj = Sale.objects.get(id=1)
        print(obj)

    # pack up data to be sent to template via context dictionary
    context = {
        'form': form,
        'sales_df': sales_df,
    }
    return render(request, 'sales/records.html', context)