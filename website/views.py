from django.shortcuts import render
from django.views import generic

from .filter import PCat_filter

from .models import PCat, PSubCat, Product


class Home(generic.list.ListView):
    template_name = "databob/home.html"
    model = PCat


    def get(self, request, *args, **kwargs):
        all_obj = PCat.objects.all()
        cat_filter = PCat_filter(request.GET, queryset=all_obj)
        

        return render(request, "databob/home.html", 
        context={
            "cat_filter":cat_filter
            })



#class Detail(generic.list.DetailView)