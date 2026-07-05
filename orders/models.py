from django.db import models
from django.contrib.auth import get_user_model
from offers.models import Offer
import uuid

User = get_user_model()
class OrderStatus(models.TextChoices):
    PAID = 'paid', 'Paid'
    DELIVERED = 'delivered', 'Delivered'
    COMPLETED = 'completed', 'Completed'
    DISPUTED = 'disputed', 'Disputed'
class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_buyer')
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='orders')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PAID)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"Order {self.id} | Buyer: {self.buyer.username} | Offer: {self.offer.title}"