from django import forms
from .models import Student


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100, help_text="Enter your First name")
    last_name = forms.CharField(max_length=100, help_text="Enter your Last name")
    email = forms.EmailField(help_text="Enter your Email address")
    password = forms.CharField(max_length=16, help_text="Enter your Password", widget=forms.PasswordInput)


class StudentForm(forms.ModelForm):

    age = forms.IntegerField(widget=forms.NumberInput)

    class Meta:
        model = Student
        fields = "__all__"


class DynamicForm(forms.Form):
    name = forms.CharField(max_length=100, help_text="Enter your Name")
    email = forms.EmailField(max_length=100, help_text="Enter your Email")