from rest_framework import viewsets
from .models import InventoryItem, Dish, InventoryUpdateLog
from .serializers import InventoryItemSerializer, DishSerializer, InventoryUpdateLogSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class InventoryUpdateLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryUpdateLog.objects.all()
    serializer_class = InventoryUpdateLogSerializer
