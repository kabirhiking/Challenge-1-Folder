from rest_framework import serializers
from .models import InventoryItem, Dish, InventoryUpdateLog

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'quantity', 'unit', 'last_updated']

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'ingredients', 'instructions', 'cuisine_type', 'taste', 'reviews', 'prep_time']

class InventoryUpdateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryUpdateLog
        fields = ['id', 'inventory_item', 'action_type', 'quantity', 'timestamp']
