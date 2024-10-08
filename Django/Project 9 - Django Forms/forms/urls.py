from django.urls import path
from .views import user_form, student_form, StudentFormView, dynamic_form, widget_form

urlpatterns = [
    path('user_form/', user_form, name='user_form'),
    path('student_form/', student_form, name='student_form'),
    path('student_form_view/', StudentFormView.as_view(), name='student_form_view'),
    path('dynamic_form/', dynamic_form, name='dynamic_form'),
    path('widget_form/', widget_form, name='widgets_form')
]