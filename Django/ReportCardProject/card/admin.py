from django.contrib import admin
from .models import (
    Department,
    StudentID,
    Student,
    Subject,
    SubjectMark
)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectMark, SubjectMarkAdmin)


