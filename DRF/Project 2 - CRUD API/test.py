import random
import requests
from faker import Faker

fake = Faker()


url = 'http://localhost:8000/api/students'


def get_student(id):

    response = requests.get(f"{url}/{id}")
    print(response.status_code)
    print(response.json())


def get_students():

    response = requests.get(url)
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


def update_student(id):
    data = {
        "name": fake.name(),
        "city": fake.city()
    }

    response = requests.put(f"{url}/{id}", json=data)
    print(response.status_code)
    print(response.json())


def delete_student(id):

    response = requests.delete(f"{url}/{id}")
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    # get_students()
    # get_student(6)
    # add_student()
    # update_student(8)
    delete_student(1)