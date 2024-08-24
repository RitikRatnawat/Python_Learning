from django.core.mail import send_mail, EmailMessage
from django.conf import settings


def send_email_to_client():
    subject = "This Email from the Django Server"
    message = "This is the Test Message from the Django Server"
    from_email = settings.EMAIL_HOST_USER
    recipients = ["<List Recipients Emails>"]

    send_mail(subject, message, from_email, recipients)


def send_email_with_attachment(file_path):
    subject = "This Email from the Django Server"
    message = "This is the Test Message from the Django Server"
    from_email = settings.EMAIL_HOST_USER
    recipients = ["<List Recipients Emails>"]

    email = EmailMessage(subject=subject, body=message, from_email=from_email, to=recipients)
    email.attach_file(file_path)

    email.send()