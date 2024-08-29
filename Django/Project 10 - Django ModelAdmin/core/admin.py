import string
from django.contrib import admin
from .models import Student

# Documentation : https://docs.djangoproject.com/en/5.1/ref/contrib/admin/


class NameListFilter(admin.SimpleListFilter):
    title = "Name Starts With"

    parameter_name = "filter_key"

    def lookups(self, request, model_admin):
        return [(ch, ch) for ch in list(string.ascii_uppercase)]

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(student_name__startswith=self.value().lower())


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "student_name", "student_email", "student_password", "created_at"]
    list_filter = [NameListFilter]
    ordering = ["student_name"]
    search_fields = ["student_name", "student_email"]
    date_hierarchy = "created_at"



admin.site.register(Student, StudentAdmin)




