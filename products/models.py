from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    
class Products(models.Model):
       
       name = models.CharField(max_length=100)
       slug =models.SlugField(unique=True)
       description =models.TextField()
       price = models.DecimalField(max_digits=10,decimal_places=2)
       image = models.ImageField(upload_to="products/")
       category =models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products",blank=True,null=True)       
       
       def __str__(self):
          return self.name
       
       
class Wishlist(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user','product')
        
    def  __str__(self):
        return f"{self.user.username} - {self.product.name}"
    
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now=True)
    
    
    class Meta :
        unique_together = ('user','product')


    def __str__(self):
        return f"{self.user.name} - {self.product.name} ({self.quantity})"