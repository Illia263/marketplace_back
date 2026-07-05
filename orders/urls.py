from .views import CreateOrderView, OrderStatusView
from django.urls import path
urlpatterns = [
    path('', CreateOrderView.as_view(), name="order"),
    path('status/<uuid:pk>/', OrderStatusView.as_view(), name='order-status')
]
