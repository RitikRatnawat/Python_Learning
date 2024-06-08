from django.contrib import admin
from django.db.models import Sum
from .models import (
    Department,
    StudentID,
    Student,
    Subject,
    SubjectMark,
    StudentRank
)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ["student", "subject", "marks"]


class StudentRankAdmin(admin.ModelAdmin):
    list_display = ["student", "rank", "total_marks", "date_of_generation"]

    def total_marks(self, obj):
        subject_marks = SubjectMark.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(marks=Sum("marks"))["marks"]
        return marks


# Register your models here.
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(SubjectMark, SubjectMarkAdmin)
admin.site.register(StudentRank, StudentRankAdmin)


