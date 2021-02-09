from rest_framework import serializers
from .models import Hero

class HeroDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

class HeroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'user')

