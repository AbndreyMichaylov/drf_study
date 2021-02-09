from django.contrib import admin
from django.urls import path, include
from .views import HeroCreateView


app_name = 'hero'
urlpatterns = [
    path('hero/create/', HeroCreateView.as_view())
]
