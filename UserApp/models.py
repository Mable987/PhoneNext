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

class CratDb(models.Model):
    UserName = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.FloatField(null=True,blank=True)
    TotalPrice = models.FloatField(null=True,blank=True)
    ProductImage = models.ImageField(upload_to= "Cart Images",null=True,blank=True)

