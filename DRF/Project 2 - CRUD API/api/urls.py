from django.urls import path
from .views import get_or_update_student, add_student


urlpatterns = [
    path('students/<int:id>', get_or_update_student, name="get_or_update_student"),
    path('students', add_student, name="add_student")
]