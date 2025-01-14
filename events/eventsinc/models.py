from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 