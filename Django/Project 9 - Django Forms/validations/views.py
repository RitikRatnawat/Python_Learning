from django.shortcuts import render
from .forms import UserRegistration


def user_registration(request):

    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            print("Form Validated successfully")
            print(form.cleaned_data["first_name"], form.cleaned_data["last_name"])

    else:
        form = UserRegistration()

    return render(request, "validations/registration.html", {"form": form})