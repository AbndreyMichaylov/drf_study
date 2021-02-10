from django.shortcuts import render
from rest_framework import generics
from .models import Hero
from .serializers import HeroDetailSerializer, HeroListSerializer

class HeroCreateView(generics.CreateAPIView):
    serializer_class = HeroDetailSerializer


class HeroListView(generics.ListAPIView):
    serializer_class  = HeroListSerializer
    queryset = Hero.objects.all()


class HeroDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeroDetailSerializer
    queryset = Hero.objects.all()