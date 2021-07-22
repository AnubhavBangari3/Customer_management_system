from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    
    added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    
    
    def __str__(self):
        return str(self.name)
    
class Product(models.Model):
    choices=(('Indoor','Indoor'),('Outdoor','Outdoor'))
    name=models.CharField(max_length=200)
    price=models.FloatField()
    category=models.CharField(max_length=200,null=True,choices=choices)
    description=models.CharField(max_length=200,null=True)
    tags=models.ManyToManyField(Tag)
    added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    
class Order(models.Model):
    choice=(('Pending','Pending'), ('Out of stock','Out of stock'),('Delivered','Delivered'))
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name="customer")
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name="product_order")
    
    added=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,choices=choice)
    
    def __str__(self):
        return str(self.product.name)
    
    
    

    
