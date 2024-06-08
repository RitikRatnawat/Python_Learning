from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import Student, SubjectMark, StudentRank


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
            return redirect("/card/students/")

    return render(request, "reports/login.html")


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

    return render(request, "reports/register.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url="/login/")
def get_students(request):
    queryset = Student.objects.all()

    if request.GET.get('search_key'):
        key = request.GET.get('search_key')
        queryset = queryset.filter(Q(student_id__student_id__icontains=key) |
                                   Q(student_name__icontains=key) |
                                   Q(student_email__icontains=key) |
                                   Q(department__dept_name__icontains=key))

    paginator = Paginator(queryset, 25)
    num_pages = range(paginator.num_pages)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, "reports/students.html", context={"students": page_obj, "num_pages": num_pages})


@login_required(login_url="/login/")
def get_student_marks(request, student_id):
    queryset = SubjectMark.objects.filter(student__student_id__student_id=student_id)
    student_name = queryset[0].student.student_name
    total_marks = queryset.aggregate(total_marks=Sum("marks"))
    current_rank = queryset.first().student.studentranks.first().rank

    context = {
        "student_name": student_name,
        "total_marks": total_marks,
        "student_marks": queryset,
        "rank": current_rank
    }
    return render(request, "reports/card.html", context=context)