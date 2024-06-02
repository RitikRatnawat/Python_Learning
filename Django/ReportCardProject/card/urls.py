from django.urls import path
from .views import get_students, get_student_marks

urlpatterns = [
    path("students/", get_students, name="students"),
    path("report_card/<str:student_id>", get_student_marks, name="student_marks")
]