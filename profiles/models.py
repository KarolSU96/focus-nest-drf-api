from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from task_collections.models import TaskCollection
from tasks.models import Task

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

@receiver(post_save, sender=Task)
def update_profile_total_tasks(sender, instance, created, **kwargs):
    if created:
        instance.owner.profile.total_tasks += 1
        if instance.is_done:
            instance.owner.profile.finished_tasks += 1
        instance.owner.profile.save()
    else:
        # Task is being updated, check if is_done has changed
        if instance.is_done and not instance.owner.profile.finished_tasks:
            instance.owner.profile.finished_tasks += 1
        elif not instance.is_done and instance.owner.profile.finished_tasks:
            instance.owner.profile.finished_tasks -= 1
        instance.owner.profile.save()  

@receiver(post_save, sender=TaskCollection)
def update_profile_total_collections(sender, instance, created, **kwargs):
    if created:
        instance.owner.profile.total_collections += 1
        instance.owner.profile.save()

@receiver(post_delete, sender=Task)
def update_profile_total_tasks_on_delete(sender, instance, **kwargs):
    instance.owner.profile.total_tasks -= 1
    instance.owner.profile.save()


@receiver(post_delete, sender=TaskCollection)
def update_profile_total_collections_on_delete(sender, instance, **kwargs):
    instance.owner.profile.total_collections -= 1
    instance.owner.profile.save()


# Signal handler to create a profile for a user when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
