from django.shortcuts import render
from rest_framework import generics
from .models import Hero
from .serializers import HeroDetailSerializer, HeroListSerializer
from .permisions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class HeroCreateView(generics.CreateAPIView):
    serializer_class = HeroDetailSerializer
    

class HeroListView(generics.ListAPIView):
    serializer_class  = HeroListSerializer
    queryset = Hero.objects.all()
    permission_classes = (IsAdminUser, )


class HeroDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HeroDetailSerializer
    queryset = Hero.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )