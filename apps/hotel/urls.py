from django.urls import path
from . import views
urlpatterns = [
    path('hotel', views.HotelView.as_view()),
    path('hotel/<int:id>', views.HotelDetail.as_view()),
    path('ratings', views.RatingView.as_view())
    
]