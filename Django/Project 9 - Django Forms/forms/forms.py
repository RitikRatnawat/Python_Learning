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
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    mobile = forms.IntegerField()
    key = forms.CharField(widget=forms.HiddenInput())


# docs : https://docs.djangoproject.com/en/5.1/ref/forms/widgets/
class WidgetsForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'cls1'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'cls1'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput())
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    age = forms.IntegerField(widget=forms.NumberInput())
    is_adult = forms.BooleanField(widget=forms.CheckboxInput())
    address = forms.CharField(max_length=500, widget=forms.Textarea())
    hidden = forms.CharField(max_length=50, widget=forms.HiddenInput())