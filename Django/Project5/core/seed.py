import random
from faker import Faker
from .models import Student


def seed_db(n=10):
    fake = Faker()

    try:
        for _ in range(n):
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()
            is_deleted = random.choice([True, False])
            print(is_deleted)

            Student.objects.create(student_name=student_name, student_email=student_email,
                                   student_age=student_age, student_address=student_address,
                                   is_deleted=is_deleted)

    except Exception as e:
        print(e)
