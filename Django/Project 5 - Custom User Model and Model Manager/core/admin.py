from django.contrib import admin
from .models import CustomUser, Student


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["student_name", "student_email", "student_age", "student_address", "is_deleted"]
    list_filter = ["student_age", "is_deleted"]

    def get_queryset(self, request):
        return self.model.admin_objects.all()


admin.site.register(CustomUser)
admin.site.register(Student, StudentModelAdmin)
