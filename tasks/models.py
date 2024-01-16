from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    is_done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    notes = models.TextField(max_length=500, blank=True)

    def __str__(self):
        
        return f"{self.owner.username}'s Task: {self.task_name}"

# Create your models here.
