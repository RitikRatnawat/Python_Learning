from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.student_name