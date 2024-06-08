from django.db import models


# Create your models here.
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


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name


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


class SubjectMark(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"

    class Meta:
        ordering = ["student"]
        unique_together = ['student', 'subject']


class StudentRank(models.Model):
    student = models.ForeignKey(Student, related_name="studentranks", on_delete=models.CASCADE)
    rank = models.IntegerField()
    date_of_generation = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.rank}"

    class Meta:
        ordering = ["rank"]
        unique_together = ['rank', 'date_of_generation']


