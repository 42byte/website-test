from django.contrib import admin
from .models import PCat, PSubCat, Product


admin.site.register([PCat, PSubCat, Product])