from django.urls import path
from .views import student_detail, all_student_details, create_student

urlpatterns = [
    path("stu-info/<int:pk>", student_detail, name="student_detail"),
    path("all-stu-info/", all_student_details, name="all_student_details"),
    path("add-stu-info/", create_student, name="add_student")
]