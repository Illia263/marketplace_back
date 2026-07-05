from rest_framework import serializers
from .models import Order, OrderStatus

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'buyer', 'offer', 'price', 'status', 'created_at')
        read_only_fields = ('buyer', 'price', 'status')     

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status')

            