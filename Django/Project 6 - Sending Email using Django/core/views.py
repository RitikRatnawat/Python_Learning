from django.shortcuts import render
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings


def send_email(request):
    send_email_to_client()
    return render(request, 'email.html')


def send_email_attachment(request):
    send_email_with_attachment(f"{settings.BASE_DIR}/test.txt")
    return render(request, 'email.html')
