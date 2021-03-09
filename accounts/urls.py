from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='register'),
    path('register/', views.register, name='register'),
]