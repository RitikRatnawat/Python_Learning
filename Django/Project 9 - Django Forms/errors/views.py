from django.shortcuts import render
from .forms import UserRegistration
from .models import UserData


def user_registration(request):

    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            print("Form Validated successfully")
            print(form.cleaned_data["first_name"], form.cleaned_data["last_name"])
            print(form.cleaned_data["password"], form.cleaned_data["rpassword"])

    else:
        form = UserRegistration()

    return render(request, "errors/registration.html", {"form": form})


def user_database(request):

    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            print("Form Validated successfully")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            userdata = UserData.objects.create(first_name=first_name, last_name=last_name, email=email)
            userdata.save()

    else:
        form = UserRegistration()

    return render(request, "errors/database.html", {"form": form})