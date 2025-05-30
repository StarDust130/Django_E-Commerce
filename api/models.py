from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


#! User Model 😊
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(
        max_length=255, blank=True, null=True,
        help_text="profile picture"
    )

    def __str__(self):
        return self.email   # Use email as the string representation of the user
 
#! Category Models 😚
class Categories(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='categories_img/', blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name 

#! Product Models 😎
class Products(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_img/', blank=True, null=True)
    featured = models.BooleanField(default=True, help_text="Is this product featured?")
    slug = models.SlugField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True, blank=True)



    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    # This will ensure that the slug is unique and follows the format "name" or "name-1", "name-2", etc.
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # Keep updating slug until it's unique
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)


#! Cart Models 😍
class Cart(models.Model):
    cart_code = models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cart_code        

#! Cart Item Models 🤭
class CartItem(models.Model):
    product = models.ForeignKey(Products, related_name="item",  on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, related_name='cartitems', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} in {self.product.name} in {self.cart.cart_code}"
