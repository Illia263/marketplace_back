from rest_framework import serializers
from .models import Category, Game

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'game')

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True, source='category_set')
    class Meta:
        model = Game
        fields = ('id', 'title', 'slug', 'logo', 'categories')

