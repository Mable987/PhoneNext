from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName = models.CharField(max_length=100, unique=True)
    Description = models.TextField()
    CategoryImage = models.ImageField(upload_to='categories')
    def __str__(self):
        return self.CategoryName

class ProductDb(models.Model):
    Category_Name = models.CharField(max_length=100)
    ProductName = models.CharField(max_length=100, unique=True)
    Description = models.TextField()
    Price = models.FloatField()
    ProductImage = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.ProductName

class ProductImageDb(models.Model):
    product = models.ForeignKey(ProductDb, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.product.ProductName