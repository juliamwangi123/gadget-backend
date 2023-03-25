from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(pre_save, sender=User)
def update_profile(instance,  **kwargs):
    
    user = instance
    if user.email != "":
        
        user.username = user.email
        
        
@receiver(post_save,sender=User)
def get_profile(sender, instance,created, **kwargs):
    
    if created:
        UserProfile.objects.create(user=instance)