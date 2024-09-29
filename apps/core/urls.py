from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Make sure the correct path to views is used

router = DefaultRouter()
router.register('stat', views.StatView, basename='figures')  # Adjusted to 'stats'

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
