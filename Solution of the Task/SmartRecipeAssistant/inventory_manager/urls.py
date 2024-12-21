from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'inventory-items', views.InventoryItemViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'inventory-update-logs', views.InventoryUpdateLogViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]
