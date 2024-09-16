from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistration


def register(request):

    if request.method == 'POST':
        form = UserRegistration(request.POST)

        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, "User registered successfully")
            messages.success(request, "User registered successfully")
            # messages.add_message(request, messages.INFO, f"Your Username is {form.cleaned_data['email']}")
            messages.info(request, f"Your Username is {form.cleaned_data['email']}")

            # Getting and Setting Messages Levels
            print(f"Current Level: {messages.get_level(request)}")
            messages.debug(request, "This is a Debug message 1")
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "This is a Debug message 2")

            # Changed Message Tags
            messages.warning(request, "Your Password is very weak")



        else:
            # messages.add_message(request, messages.ERROR, "User registration failed")
            messages.error(request, "User registration failed")

    else:
        form = UserRegistration()

    return render(request, "core/user_registration.html", {'form': form})

