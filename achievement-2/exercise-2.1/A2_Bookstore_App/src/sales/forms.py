from django import forms

CHART__CHOICES = (
    # Specify choices as a tuple
    # When user selects "Bar chart" it is stored as #1
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class SalesSearchForm(forms.forms):
    book_title = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)