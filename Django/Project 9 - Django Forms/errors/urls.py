from django.urls import path
from .views import user_registration, user_database

urlpatterns = [
    path("register/", user_registration, name="error_registration"),
    path("database/", user_database, name="user_database"),
]