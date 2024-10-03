from django.urls import path
from .views import cud_student, add_student, get_students


urlpatterns = [
    path('students', get_students, name='get_students'),
    path('students/<int:id>', cud_student, name="cud_student"),
    path('students', add_student, name="add_student")
]