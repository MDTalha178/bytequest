"""
urls.py used for product
"""
from django.urls import path, include
from rest_framework import routers

from .views import ProductViewset

router = routers.DefaultRouter()
router.register('product', ProductViewset, basename='product')

urlpatterns = [
    path(r'product/', include(router.urls)),
]
