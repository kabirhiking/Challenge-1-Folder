from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"

class Dish(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()  
    instructions = models.TextField()
    cuisine_type = models.CharField(max_length=50)
    taste = models.CharField(max_length=50)
    reviews = models.TextField()
    prep_time = models.IntegerField()  
    def __str__(self):
        return self.name

class InventoryUpdateLog(models.Model):
    ACTION_TYPES = (
        ('Add', 'Add'),
        ('Remove', 'Remove'),
    )
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50, choices=ACTION_TYPES)
    quantity = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} {self.quantity} of {self.inventory_item.name}"
