from django.db import models
from django.contrib.auth.models import User


class TaskCollection(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.owner.username}'s Task Colleciton{self.title}"
