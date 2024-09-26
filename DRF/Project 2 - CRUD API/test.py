import random
import requests
from faker import Faker

fake = Faker()


url = 'http://localhost:8000/api/student'


def get_student(id):

    response = requests.get(f"{url}/{id}")
    print(response.status_code)
    print(response.json())


def add_student():
    data = {
        "name": fake.name(),
        "roll_number": random.randint(106, 500),
        "city": fake.city()
    }

    response = requests.post(url, data=data)
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    # get_student(6)
    add_student()