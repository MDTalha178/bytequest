"""
this file serialize data
"""
from rest_framework import serializers
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    product serializer
    """
    product_name = serializers.CharField(required=True, max_length=250, allow_blank=False, allow_null=False)
    product_price = serializers.IntegerField(required=True, allow_null=False)
    product_category = serializers.CharField(required=False, default='74749d0b-1aab-4fb8-a6e0-40c9389e5276')

    @staticmethod
    def validate_product_name(value):
        """
        validate product al ready exists
        :return: value
        """
        if Product.objects.filter(product_name__iexact=value).exists():
            raise serializers.ValidationError({'product-error': 'Product Already Exists'})
        return value

    def create(self, validated_data):
        category = Category.objects.filter(id=validated_data['product_category']).first()
        validated_data['product_category'] = category
        instance = Product.objects.create(**validated_data)
        instance.save()
        return instance

    class Meta:
        """
        class meat for product
        """
        model = Product
        fields = ('product_name', 'product_price', 'product_category')


class GetProductSerializer(serializers.ModelSerializer):
    """
    get product list serializer
    """

    class Meta:
        model = Product
        fields = '__all__'


class EditProductSerializer(serializers.ModelSerializer):
    """
    update product serializer
    """
    product_name = serializers.CharField(required=True, max_length=250)
    product_price = serializers.IntegerField(required=False)

    def update(self, instance, validated_data):
        instance.product_name = validated_data['product_name']
        instance.product_price = validated_data['product_price']
        instance.save()
        return instance

    class Meta:
        """
        meta class update product
        """
        model = Product
        fields = ('product_name', 'product_price')
