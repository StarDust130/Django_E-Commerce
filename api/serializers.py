from rest_framework import serializers
from .models import Categories , Products , CustomUser

#! Products Serializer 😮
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ['id', 'name', 'description', 'price', 'image', 'slug']



#! Categories Serializer 🫠
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

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