from django.urls import path
from . import views

urlpatterns = [
    path("", views.send_email, name="send_email"),
    path("attach/", views.send_email_attachment, name="send_email_attachment")
]