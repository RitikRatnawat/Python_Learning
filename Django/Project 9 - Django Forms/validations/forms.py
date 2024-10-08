from django import forms
from django.core import validators


def validate_email_domain(email):
    if not email.lower().endswith("example.com"):
        raise forms.ValidationError("Not a valid email address domain")


class UserRegistration(forms.Form):
    first_name = forms.CharField(max_length=50,
                                 validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(15)])
    last_name = forms.CharField(max_length=50,
                                validators=[validators.MinLengthValidator(4), validators.MaxLengthValidator(15)])
    email = forms.EmailField(max_length=50, validators=[validate_email_domain])
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    rpassword = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(UserRegistration, self).clean()

        password = cleaned_data['password']
        rpassword = cleaned_data['rpassword']

        if password != rpassword:
            raise forms.ValidationError("Password mismatch")

        return cleaned_data

    # def clean_password(self):
    #     password_val = self.cleaned_data['password']
    #     first_name = self.cleaned_data['first_name']
    #     last_name = self.cleaned_data['last_name']
    #
    #     if len(password_val) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters")
    #
    #     if first_name.lower() in password_val or last_name.lower() in password_val:
    #         raise forms.ValidationError("Name should not be the part of the password")
    #
    #     return password_val
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #
    #     first_name = cleaned_data["first_name"]
    #     if len(first_name) < 4:
    #         raise forms.ValidationError("First name must be at least 4 characters")
    #
    #     last_name = cleaned_data["last_name"]
    #     if len(last_name) < 4:
    #         raise forms.ValidationError("Last name must be at lease 4 characters")
    #
    #     email = cleaned_data["email"]
    #     if not email.endswith("example.com"):
    #         raise forms.ValidationError("Not a valid email address")
    #
    #     return cleaned_data
