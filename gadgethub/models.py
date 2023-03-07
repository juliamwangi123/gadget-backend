from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, max_length=1000,null=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    reviewsNum = models.IntegerField(null=True, blank=True ,default=0)
    rating = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    stockCount = models.IntegerField(null=True, blank=True,default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.title
    
    
    
  
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, default=0,blank=True)
    
    
    def __str__(self):
        
        return self.rating
    
class Order(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200,null=True, blank=True)
    taxPrice = models.DecimalField(max_digits=7,decimal_places=2,null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7,decimal_places=2,null=True , blank=True)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    deliveredAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        
        return self.createdAt
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(null=True, default=0,blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.CharField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        
        return self.name
    
    
    
class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address =  models.CharField(max_length=200, null=True, blank=True)
    city =  models.CharField(max_length=200, null=True, blank=True)
    country =  models.CharField(max_length=200, null=True, blank=True)
    
    
    def __str__(self):
        
        return self.address
    
    
    
    
    
    
    
    
    
    
    
    