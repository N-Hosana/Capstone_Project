from datetime import timezone
from rest_framework import serializers
from .models import Event, Attendee
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
  attendees = serializers.StringRelatedField(many=True, read_only=True)
waitlist = serializers.StringRelatedField(many=True, read_only=True)
class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date_time', 'location', 'organizer', 'capacity', 'created_date','attendees','waitlist']

def validate_date_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value
   
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'event', 'user']
