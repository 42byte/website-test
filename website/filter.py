from .models import PCat
import django_filters
from django import forms



#https://simpleisbetterthancomplex.com/tutorial/2016/11/28/how-to-filter-querysets-dynamically.html
#https://django-filter.readthedocs.io/en/master/

class PCat_filter(django_filters.FilterSet):
    #the name here must be the same as in the db to actually filter for the inpt of the user
    #if its not the same name, the filter cannot applied to the column
    cat = django_filters.ModelMultipleChoiceFilter(to_field_name="cat", queryset = PCat.objects.all(), widget = forms.CheckboxSelectMultiple)
    

    #define here which model should be used and what columns (fields) should be filtered.
    class Meta:
        model = PCat
        fields = ["cat", "upvotes",]