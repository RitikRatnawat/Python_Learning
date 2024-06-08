import random
from faker import Faker
from django.db.models import Sum
from .models import (
    Department,
    Student,
    StudentID,
    Subject,
    SubjectMark,
    StudentRank
)

fake = Faker()


def create_subject_marks(n=10):

    try:
        students = Student.objects.all()

        for student in students:
            subjects = Subject.objects.all()

            for subject in subjects:
                SubjectMark.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100)
                )

    except Exception as e:
        print(e)


def seed_db(n=10):

    departments = Department.objects.all()

    try:
        for _ in range(n):
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()

            dept_index = random.randint(0, len(departments) - 1)

            student_id = f"STU-0{random.randint(100, 999)}"

            obj = StudentID.objects.create(student_id=student_id)

            Student.objects.create(student_name=student_name, student_email=student_email,
                                   student_age=student_age, student_address=student_address,
                                   department=departments[dept_index], student_id=obj)

    except Exception as e:
        print(e)


def generate_ranks():
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', '-student_age')
    i = 1

    for rank in ranks:
        StudentRank.objects.create(
            student=rank,
            rank=i
        )
        i += 1