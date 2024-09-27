from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('booking', views.Book, basename='booking')

urlpatterns = [
    path('hotel', views.HotelView.as_view()),
    path('hotel/<int:id>', views.HotelDetail.as_view()),
    path('ratings', views.RatingView.as_view()),
    path('', include(router.urls))
    
]