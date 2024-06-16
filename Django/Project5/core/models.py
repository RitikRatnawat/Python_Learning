from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'email']
    objects = CustomUserManager()


