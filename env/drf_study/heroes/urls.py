from django.contrib import admin
from django.urls import path, include
from .views import HeroCreateView, HeroListView, HeroDetailView


app_name = 'hero'
urlpatterns = [
    path('hero/create/', HeroCreateView.as_view()),
    path('all/', HeroListView.as_view()),
    path('hero/detail/<int:pk>/', HeroDetailView.as_view())
]
