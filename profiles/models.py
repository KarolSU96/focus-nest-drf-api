from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):

    # Link each profile to a user through a one-to-one relationship
    owner = models.OneToOneField(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_d7stiw'
    )
    total_tasks = models.PositiveIntegerField(default=0)
    total_collections = models.PositiveIntegerField(default=0)
    finished_tasks = models.PositiveIntegerField(default=0)
    current_goals = models.CharField(max_length=500, blank=True)

    class Meta: 
        # Specify the default ordering for profiles based on creation time
        ordering = ['-created_at']


    def __str__(self):
        return f"{self.owner.username}'s profile"

# Signal handler to create a profile for a user when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
