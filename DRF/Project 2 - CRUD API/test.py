import json
import requests


url = 'http://localhost:8000/api/student'


def get_student(id):
    data = {}
    if id is not None:
        data["id"] = id

    json_data = json.dumps(data)
    response = requests.get(url, data=json_data)
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    get_student(1)