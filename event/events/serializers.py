from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = Event
        fields = '__all__'
        fields = ['id', 'title', 'description', 'event_date', 'created_at', 'created_by']
