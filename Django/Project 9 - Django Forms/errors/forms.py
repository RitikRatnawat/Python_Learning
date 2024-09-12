from django import forms
from django.core import validators


def validate_email_domain(email):
    if not email.lower().endswith("example.com"):
        raise forms.ValidationError("Not a valid email address domain")


class UserRegistration(forms.Form):
    error_css_class = "error"
    required_css_class = "required"
    first_name = forms.CharField(max_length=50,
                                 validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(15)],
                                 error_messages={"required": "Enter Your First Name"})
    last_name = forms.CharField(max_length=50,
                                validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(15)],
                                error_messages={"required": "Enter Your Last Name"})
    email = forms.EmailField(max_length=50, validators=[validate_email_domain],
                             error_messages={"required": "Enter Your Email"})