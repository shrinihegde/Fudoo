from django.db import models
from django.contrib.auth.models import User
# Create your models here.


LOGIN_TYPES=((1,("Store Manager")),
            (2,("User")))

class FoodCourt(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(null=True,blank=True,max_length=100)
    foodcourt_image = models.ImageField(null=True, blank=True, upload_to="foodcourt-images/")
    fc_id=models.CharField(max_length=50)
    category=models.CharField(null=True,blank=True,max_length=200)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField(default=0)
    empid=models.IntegerField(default=0)
    dob=models.DateField(null=True)
    user_type=models.CharField(choices=LOGIN_TYPES,max_length=100,default=2)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Store(models.Model):
    foodcourt=models.ForeignKey(FoodCourt,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=50)
    cover=models.ImageField(null=True, blank=True, upload_to="pics/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    rating=models.FloatField(default=0)

    def __str__(self):
        return self.name

class MenuCatalog(models.Model):
    store=models.ForeignKey(Store,on_delete=models.CASCADE,default=1)
    menu=models.CharField(max_length=100)

    def __str__(self):
        return self.menu

class Item(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0)
    cuisine=models.CharField(max_length=100,null=True,blank=True)
    menu=models.ForeignKey(MenuCatalog,on_delete=models.CASCADE,default=1) 
    store=models.ForeignKey(Store,on_delete=models.CASCADE,default=1)
    is_available=models.BooleanField(default=True) 
    description=models.TextField(max_length=200,null=True,blank=True)
    rating=models.FloatField(default=0)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

