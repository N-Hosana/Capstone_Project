from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    waitlist = models.ManyToManyField(User, related_name="waitlist_events", blank=True)

    def __str__(self):
        return self.title

    def is_full(self):
        return self.capacity <= self.attendees.count()

    def available_spots(self):
        return max(self.capacity - self.attendees.count(), 0)


class Attendee(models.Model):
    event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
