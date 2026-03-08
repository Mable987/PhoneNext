from django.db import models

# Create your models here.
class ContactDb(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class RegistrationDb(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)

class CartDb(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.FloatField(null=True,blank=True)
    TotalPrice = models.FloatField(null=True,blank=True)
    ProductImage = models.ImageField(upload_to= "Cart Images",null=True,blank=True)

class OrderDb(models.Model):
    FirstName = models.CharField(max_length=100,null=True,blank=True)
    LastName = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Mobile  = models.IntegerField(max_length=100,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    PinCode = models.CharField(max_length=100,null=True,blank=True)
    TotalPrice = models.FloatField(null=True,blank=True)

