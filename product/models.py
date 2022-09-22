"""
model file for creating a table in database
"""
# Third party imports
import uuid
from django.db import models


class Category(models.Model):
    """
    to create category for product in table or model in database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=250, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


class Product(models.Model):
    """
    to create field in Product table or model in database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=250, blank=False, null=False)
    product_price = models.IntegerField(max_length=15, blank=False, null=False)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
