from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('gallery/', views.gallery, name="gallery"),
    path('profile/<str:pk>/', views.profile, name="profile"),

]

