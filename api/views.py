from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products
from .serializers import ProductListSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

api_view(['GET'])
def product_list(request):
    products = Products.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    print("Serializer 😆", serializer)  
    return Response(serializer.data)


