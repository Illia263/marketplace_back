from django.shortcuts import render
from .serializers import OrderSerializer, OrderStatusSerializer
from rest_framework import generics
from .models import Order, OrderStatus
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError

class CreateOrderView (generics.ListCreateAPIView):
     permission_classes = [IsAuthenticated]
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     def perform_create(self, serializer):
          buyer = self.request.user
          target_offer = serializer.validated_data.get('offer')
          if buyer.balance >= target_offer.price:
               buyer.balance -= target_offer.price
               buyer.save()
               target_offer.stock -= 1
          
          elif buyer.balance < target_offer.price:
               raise ValidationError({"error" : "Not enough funds"})
          
          if target_offer.stock <= 0:
               target_offer.is_active = False
          target_offer.save()
          serializer.save(buyer=buyer, price=target_offer.price)
class OrderStatusView (generics.RetrieveUpdateAPIView):
     permission_classes = [IsAuthenticated]
     serializer_class = OrderStatusSerializer
     def get_queryset(self):
          return Order.objects.filter(buyer=self.request.user)
     def perform_update(self, serializer):
          instance = serializer.instance
          status = serializer.validated_data.get('status')
          seller = instance.offer.seller

          if status == 'completed':
               seller.balance += instance.price 
               seller.save()
               serializer.save()
          elif status == "disputed":
               serializer.save()
          else:
               serializer.save()


