from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import UserProfile,Order,OrderItem

@receiver(pre_save, sender=User)
def update_profile(instance,  **kwargs):
    
    user = instance
    if user.email != "":
        
        user.username = user.email
        
        
@receiver(post_save,sender=User)
def get_profile(sender, instance,created, **kwargs):
    
    if created:
        UserProfile.objects.create(user=instance)
        
        
        
@receiver(post_save, sender=Order)
def update_order_items(sender, instance, **kwargs):
    if instance.isPaid:
        instance.orderitem_set.update(isPaid=True)
        
        
        
@receiver(post_save, sender=Order)
def update_order(sender, instance, **kwargs):
    if instance.orderNumber:
        instance.orderitem_set.update(orderItemNumber=instance.orderNumber)
        
        
        
@receiver(post_save, sender=Order)
def mark_product_as_sold(sender, instance, **kwargs):
    if instance.isPaid:
        
        
        instance.product_set.update(isSold=instance.isPaid)
