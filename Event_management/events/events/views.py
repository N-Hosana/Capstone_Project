from rest_framework import viewsets
from ..eventsinc.models import Event
from ..eventsinc.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)
