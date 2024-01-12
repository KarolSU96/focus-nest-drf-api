from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_d7stiw'
    )


    class Meta: 
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.owner}'s profile"
# Create your models here.
