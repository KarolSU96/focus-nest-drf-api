from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class User(models.Models):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharFiled(max_length=30, unique= True)
    email = models.EmailField(unique=True)


    class Meta:
        ordering = ['-created_at']

    
    def __str__(self):
        return f"User: {self.owner}"

def create_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create(owner=instance)

post_save.connect(create_user, sender=User)






# Create your models here.
