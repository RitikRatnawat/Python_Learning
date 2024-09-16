from django import forms
from .models import User


class UserRegistration(forms.ModelForm):

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = "__all__"