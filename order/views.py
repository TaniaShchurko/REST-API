from rest_framework import viewsets
from .serializer import OrderSerializer
from .models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('book')
    serializer_class = OrderSerializer