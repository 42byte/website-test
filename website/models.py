from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class PCat(models.Model):
    cat = models.CharField(max_length=100)
    img = models.ImageField(upload_to="PCat_img/", blank=True, default="PCat_img/test.jpg")
    content = models.TextField(blank=True)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.cat

class PSubCat(models.Model):
    cat = models.ForeignKey(PCat, on_delete = models.SET_DEFAULT, default = 0)
    subcat = models.CharField(max_length=100)
    img = models.ImageField(upload_to="PSubCat_img/", blank=True)
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


class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    bio = models.TextField()
    products_watchlist = models.ManyToManyField(Product)

    def __str__(self):
        return self.username


#signal that creates a UserProfile everytime a new User is created. 
def create_user_profile(sender, **kwargs):
    if kwargs["created"]:
        user_profil = UserProfile.objects.create(user=kwargs["instance"])

post_save.connect(create_user_profile, sender = User)





class Product_Commments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete = models.SET_DEFAULT, default = "none")

    def __str__(self):
        return self.product



