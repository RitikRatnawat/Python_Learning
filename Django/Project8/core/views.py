from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Employee
from .forms import EmployeeForm


class EmployeeCreateView(CreateView):

    model = Employee
    fields = "__all__"

    def get_success_url(self):
        return reverse('employee_detail', kwargs={'pk': self.object.pk})


class EmployeeListView(ListView):

    model = Employee

    def get_queryset(self, *args, **kwargs):
        qs = super(EmployeeListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-last_name")
        return qs


class EmployeeDetailView(DetailView):

    model = Employee


class EmployeeUpdateView(UpdateView):

    model = Employee
    fields = "__all__"

    def get_success_url(self):
        return reverse('employee_detail', kwargs={'pk': self.object.pk})