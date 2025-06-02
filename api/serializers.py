from rest_framework import serializers
from .models import Categories , Products , CustomUser , CartItem , Cart

#! Products Serializer 😌(Show Products in Home Page)
class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'image', 'slug']

#! Products Detail Serializer 😮(Show Product Details in Product Page)
class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'price', 'image', 'description', 'category', 'slug']

#! Categories Serializer 😚(Show Categories in Home Page)
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'image' , "slug"]


#! Categories Detail Serializer 🫠(Show Categories in Home Page)
class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = ['id', 'name', 'image', 'products']


#! Custom User Serializer 😎
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_picture_url']
        read_only_fields = ['id', 'username']  # Make id and username read-only

    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data.
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data.get('password', None),
            profile_picture_url=validated_data.get('profile_picture_url', None)
        )
        return user

#! Cart Item Serializer 🤭
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    sub_total = serializers.SerializerMethodField()
     
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity' , "sub_total"]

    def get_sub_total(self, cartitem):
        return cartitem.product.price * cartitem.quantity    


#! Cart Serializer 😜
class CartSerializer(serializers.ModelSerializer):
    carditems = CartItemSerializer(many=True, read_only=True)
    card_total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'cart_code', 'carditems' ,"card_total"]

    def get_card_total(self, cart):
        items = cart.carditems.all()
        total = sum(item.product.price * item.quantity for item in items)
        return total
    

#! Cart Stat Serializer 🤠
class CartStatSerializer(serializers.ModelSerializer):
    total_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "cart_code", "total_quantity"]

    def get_total_quantity(self, cart):
        items = cart.cartitems.all()
        total = sum([item.quantity for item in items])
        return total

