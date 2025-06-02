from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartItem, Products, Categories, Cart
from .serializers import CartItemSerializer, ProductListSerializer, ProductDetailSerializer , CategoryListSerializer
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


#! Product Detail View 🙃(Show Product Details irn Product Page)
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

#! Add to Cart View 🛒(Add Product to Cart)


@api_view(['POST'])
def add_to_cart(request):
    cart_code = request.data.get('cart_code')
    product_id = request.data.get('product_id')

    if not cart_code or not product_id:
        return Response({"error": "cart_code and product_id are required"}, status=400)

    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    cart, _ = Cart.objects.get_or_create(cart_code=cart_code)
    cartitem, created = CartItem.objects.get_or_create(
        product=product, cart=cart)

    if not created:
        cartitem.quantity += 1  # increment quantity if already in cart
    else:
        cartitem.quantity = 1

    cartitem.save()
    serializer = CartItemSerializer(cartitem)
    return Response(serializer.data)


#! Update Cart Item Quantity View 🛍️(Update Quantity of Cart Item) 
@api_view(['PUT'])
def update_cartitem_quantity(request):
    cartitem_id = request.data.get("item_id")
    quantity = request.data.get("quantity")

    quantity = int(quantity)

    cartitem = CartItem.objects.get(id=cartitem_id)
    cartitem.quantity = quantity
    cartitem.save()

    serializer = CartItemSerializer(cartitem)
    return Response({"data": serializer.data, "message": "Cartitem updated successfully!"})



#! View Cart Items View 🛍️(View Cart Items)
@api_view(['GET'])
def view_cart(request):
    cart_code = request.query_params.get('cart_code')

    if not cart_code:
        return Response({"error": "cart_code is required"}, status=400)

    try:
        cart = Cart.objects.get(cart_code=cart_code)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=404)

    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)

    grand_total = sum(
        [item.product.price * item.quantity for item in cart_items])

    return Response({
        "items": serializer.data,
        "grand_total": grand_total
    })
