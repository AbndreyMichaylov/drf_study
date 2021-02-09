from django.shortcuts import render
from rest_framework import generics
from .serializers import HeroDetailSerializer

class HeroCreateView(generics.CreateAPIView):
    serializer_class = HeroDetailSerializer