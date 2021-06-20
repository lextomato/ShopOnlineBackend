from django.shortcuts import render
 
# Elemnts required for the REST API to work
from rest_framework import viewsets, filters
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
 
# Class 'ProductsSerializer' and 'CategorySerializer'
from product.serializers import ProductSerializer, CategorySerializer
 
# Models 'Product' and 'Category
from product.models import Product, Category
 
### Creating views for the REST API ###

# View of the categories
class CategoryViewSet(viewsets.ModelViewSet):    
    
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer

# View of the products
class FilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # System Filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
