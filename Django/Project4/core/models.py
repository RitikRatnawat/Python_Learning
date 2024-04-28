from django.db import models


class Department(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_description = models.TextField()
    employee_count = models.IntegerField(default=1)

    def __str__(self):
        return self.dept_name

    class Meta:
        ordering = ['dept_name']


class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id


class Student(models.Model):
    department = models.ForeignKey(Department, related_name="dept", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="student1_id", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ["student_name"]
        verbose_name = "student"


"""
Department.objects.all().order_by("<attribute_name>") returns queryset of objects in ascending order.
Department.objects.all().order_by("-<attribute_name>") returns queryset of objects in descending order when we put 
                                                        -(minus) sign before the attribute name.
Department.objects.filter(attribute_name = value) returns a filtered queryset of objects and also works with field
                                                        lookups such as __in, __gte, __lt, __exists etc.
"""