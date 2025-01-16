from datetime import timezone
from rest_framework import viewsets
from eventsinc.models import Attendee, Event
from eventsinc.serializers import EventSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def get_queryset(self):
        if self.action in ['list', 'retrieve']:
            return Event.objects.filter(date_time__gte=timezone.now())
        return self.queryset.filter(organizer=self.request.user)

    @action(detail=True, methods=['post'])
    def join_event(self, request, pk=None):
        event = self.get_object()
        if event.is_full():
            event.waitlist.add(request.user)
            return Response({'message': 'Added to waitlist'}, status=status.HTTP_200_OK)
        Attendee.objects.create(event=event, user=request.user)
        return Response({'message': 'Joined event'}, status=status.HTTP_200_OK)



@csrf_exempt
def api_signup(request):
    """Handle user signup."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)

            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'message': f'User {user.username} created successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
def signup(request):
    return render(request, 'signup.html')

@csrf_exempt
def api_login(request):
    """Handle user login."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')

            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                return JsonResponse({'message': 'Login successful'}, status=200)
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid method'}, status=405)
def login(request):
    return render(request, 'login.html')

@csrf_exempt
def api_list(request):
    """List all users."""
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username')  # Retrieve users
        user_list = list(users)  # Convert QuerySet to a list
        return JsonResponse({'users': user_list}, status=200)
    return JsonResponse({'error': 'Invalid method'}, status=405)



