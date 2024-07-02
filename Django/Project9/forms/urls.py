from django.urls import path
from .views import user_form, student_form, StudentFormView

urlpatterns = [
    path('user_form/', user_form, name='user_form'),
    path('student_form/', student_form, name='student_form'),
    path('student_form_view/', StudentFormView.as_view(), name='student_form_view')
]