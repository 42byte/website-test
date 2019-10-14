from django.shortcuts import render
from django.views import generic

from .models import PCat, PSubCat, Product

class Home(generic.list.ListView):
    template_name = "databob/home.html"
    model = PCat

    def get(self, request, *args, **kwargs):
        return render(request, "databob/home.html", context={"categories":PCat.objects.all})        