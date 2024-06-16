from django.shortcuts import render
from .utils import send_email_to_client


def send_email(request):
    send_email_to_client()
    return render(request, 'email.html')
