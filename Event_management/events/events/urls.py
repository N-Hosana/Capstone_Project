from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, api_login, api_signup, api_list
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
def home(request):
    return HttpResponse("Welcome to the Event Management API!")

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),  
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
     path('login/', views.login, name='login'),
    path('login/', views.login, name='login'),  # Define a login view
    path('signup/', views.signup, name='signup'),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', api_login, name='api-login'),
    path('api/signup/', api_signup, name='signup'),  # Add signup route
    path('api/users/', api_list, name='api-list'),       # Add users list route
    path('api/upcoming-events/', EventViewSet.as_view({'get': 'list'}), name='upcoming-events'),
]
