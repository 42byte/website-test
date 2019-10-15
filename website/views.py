from django.shortcuts import render
from django.views import generic

from .filter import PCat_filter

from .models import PCat, PSubCat, Product, Product_Commments, UserProfile


class Home(generic.list.ListView):
    template_name = "databob/home.html"
    model = PCat


    def get(self, request, *args, **kwargs):
        all_obj = PCat.objects.all()
        cat_filter = PCat_filter(request.GET, queryset=all_obj)
        comments = Product_Commments.objects.all()

        return render(request, self.template_name, 
            context={
                "cat_filter":cat_filter,
                "comments": comments
                })





class ProductDetail(generic.detail.DetailView):
    template_name = "databob/product_detail.html"
    model = Product

    def get(self, request, pk=None, **kwargs):
        if pk:
            comments = Product_Commments.objects.all().filter(product=pk)
            #self.object = self.get_object() 
            #context_pk = super().get_context_data(**kwargs)
            return render(request, self.template_name, context={
                "product": Product.objects.get(pk=pk),
                "comments": comments
                })
        else:
            return render(request, "<h1>error</h1>")


#class ProfileDetail(generic.detail.DetailView):