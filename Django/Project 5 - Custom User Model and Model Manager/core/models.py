from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager, StudentManager


class CustomUser(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    description = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['password', 'email']
    objects = CustomUserManager()


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)

    objects = StudentManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.student_name


