from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .filter import PCat_filter
from .models import PCat, PSubCat, Product, Product_Commments, UserProfile



#______________________________________________________________
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




#_______________________________________________________________

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


#______________________________________________________________
class UserDetail(generic.detail.DetailView):
    template_name = "databob/user_detail.html"
    model = UserProfile

    def get(self, request, pk=None, **kwargs):
        if pk:
            comments = Product_Commments.objects.all().filter(user=pk)
            user = UserProfile.objects.get(pk=pk)

            return render(request, self.template_name, context={
                "user": user,
                "comments": comments
            })
        else: 
            return render(request, "<h1>error</h1>")


def register(request):
    if request.method == "POST":      
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("databob-home")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages}")


    form = UserCreationForm
    return render(request, 
            "databob/register.html", 
            context={"form":form})


def logout_user(request):
    logout(request)
    messages.info(request, f"Logged out sucessfully")
    return redirect("databob-home")


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("databob-home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, "databob/login.html", context={"form":form})



