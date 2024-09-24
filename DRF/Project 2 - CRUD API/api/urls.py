from django.urls import path
from .views import get_student


urlpatterns = [
    path('student/<int:id>', get_student, name="get_student")
]