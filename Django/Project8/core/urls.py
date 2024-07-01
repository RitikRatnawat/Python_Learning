from django.urls import path
from .views import EmployeeCreateView, EmployeeListView, EmployeeDetailView, EmployeeUpdateView

urlpatterns = [
    path("create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("list/", EmployeeListView.as_view(), name="employee_list"),
    path("detail/<int:pk>", EmployeeDetailView.as_view(), name="employee_detail"),
    path("update/<int:pk>", EmployeeUpdateView.as_view(), name="employee_update"),
]