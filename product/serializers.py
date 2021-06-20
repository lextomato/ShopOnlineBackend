from rest_framework import serializers
from product.models import Product, Category

### serializer to be able to create database views in REST API ###

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'url_image', 'price', 'discount', 'category']

# Categories serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
