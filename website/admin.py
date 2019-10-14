from django.contrib import admin
from .models import PCat, PSubCat, Product, Product_Commments, UserProfile


admin.site.register([PCat, PSubCat, Product, Product_Commments, UserProfile])