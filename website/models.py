from django.db import models


class PCat(models.Model):
    cat = models.CharField(max_length=100)
    img = models.ImageField(upload_to="PCat_img/")
    content = models.TextField(blank=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.cat

class PSubCat(models.Model):
    cat = models.ForeignKey(PCat, on_delete = models.SET_DEFAULT, default = 0)
    subcat = models.CharField(max_length=100)
    img = models.ImageField(upload_to="PSubCat_img/")
    content = models.TextField(blank=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.subcat

class Product(models.Model):
    subcat = models.ForeignKey(PSubCat, on_delete = models.SET_DEFAULT, default = 0)
    img = models.ImageField(upload_to="Product_img/", blank=True)
    GTIN = models.CharField(max_length=20)
    Name = models.CharField(max_length=100)
    Brand = models.CharField(max_length=50)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.gtin


""" class Commments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
 """