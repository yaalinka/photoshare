from django.urls import path
from .views import *

urlpatterns = [
    path('', gallery, name='gallery'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerUser, name='register'),
    path('photo/<str:pk>', viewPhoto, name='photo'),
    path('add/', addPhoto, name='add'),
]
