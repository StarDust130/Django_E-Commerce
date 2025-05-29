from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products , Categories
from .serializers import ProductListSerializer, ProductDetailSerializer , CategoryListSerializer
from django.shortcuts import get_object_or_404

# List -> Home Page 
# Detail -> Product Page

#! Product List View 😮‍💨(Show Products in Home Page)
@api_view(['GET'])
def product_list(request):
    products = Products.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    print("Serializer 😆", serializer)  
    return Response(serializer.data)


#! Product Detail View 🙃(Show Product Details in Product Page)
@api_view(['GET'])
def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)


#! Category List View 🫠(Show Categories in Home Page)
@api_view(['GET'])
def category_list(request):
    categories = Categories.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

#! Category Detail View 😚(Show Categories in Home Page)
@api_view(['GET'])
def category_detail(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    serializer = CategoryListSerializer(category)
    return Response(serializer.data)
