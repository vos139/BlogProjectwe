from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'firsthome'),
    path('about/', views.about, name = 'about'),
    ]
