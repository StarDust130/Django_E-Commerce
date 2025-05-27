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
 