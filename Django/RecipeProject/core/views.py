from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe


@login_required(login_url="/login")
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = files.get('recipe_image')

        Recipe.objects.create(recipe_name=recipe_name, recipe_description=recipe_description, recipe_image=recipe_image)

        return redirect('recipe_add')

    queryset = Recipe.objects.all()
    search_key = request.GET.get('search_recipe')

    if search_key:
        queryset = Recipe.objects.filter(recipe_name__icontains=search_key)

    context = {'recipes': queryset}
    return render(request, "recipes.html", context)


@login_required(login_url="/login")
def recipe_update(request, recipe_id):

    recipe_obj = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        data = request.POST
        files = request.FILES

        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = files.get('recipe_image')

        if recipe_obj.recipe_name != recipe_name:
            recipe_obj.recipe_name = recipe_name

        if recipe_obj.recipe_description != recipe_description:
            recipe_obj.recipe_description = recipe_description

        if recipe_image:
            recipe_obj.recipe_image = recipe_image

        recipe_obj.save()

        return redirect('recipe_add')

    context = {"recipe": recipe_obj}
    return render(request, "recipes_update.html", context)


@login_required(login_url="/login")
def recipe_delete(request, recipe_id):

    recipe_obj = get_object_or_404(Recipe, pk=recipe_id)
    recipe_obj.delete()

    return redirect('recipe_add')


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(request, user)
            return redirect("/recipe/add/")

    return render(request, "login.html")


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already exists")
            return redirect('/register/')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()

        messages.success(request, "Account registered successfully")
        return redirect('/register/')

    return render(request, "register.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')