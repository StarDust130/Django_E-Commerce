from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(
        max_length=255, blank=True, null=True,
        help_text="profile picture"
    )

    def __str__(self):
        return self.email   # Use email as the string representation of the user
 

class Categories(models.Model):
    """
    Model representing a product category.
    """
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='categories_img/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name 

class Products(models.Model):
    """
    Model representing a product.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products_img/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.SET_NULL)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name