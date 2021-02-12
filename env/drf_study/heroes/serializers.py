from rest_framework import serializers
from .models import Hero

class HeroDetailSerializer(serializers.ModelSerializer):
    #Проводит запросы к от лица вторизованного юзера, если не авторизован
    #выдает исключение
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Hero
        fields = '__all__'

class HeroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ('id', 'name', 'user')

