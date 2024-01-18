"""Learning about the Requests Module in the Python."""

import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"
headers = {'Content-type': 'application/json; charset=UTF-8'}

if __name__ == "__main__":

    # GET request
    response = requests.get(API_URL, headers=headers, timeout=90)

    print()
    if response.status_code == 200:
        print("GET Method Successful")
        print("----------"*5)
        data = response.json()
        for post in data[:5]:
            print(post)

    # POST request
    json_data = {
        "title": "Python Requests Module",
        "body": "Learning Python requests module in the Python.",
        "userId": 2156
    }

    response = requests.post(API_URL, headers=headers, json=json_data, timeout=90)

    print()
    if response.status_code == 201:
        print("POST Method Successful.")
        print("----------"*5)
        data = response.json()
        print(data)

    # PUT request
    json_data = {
        "id": 1,
        "title": "Requests Module in Python",
        "body": "Learning Python requests module in the Python.",
        "userId": 1
    }

    response = requests.put(API_URL + "/1", headers=headers, json=json_data, timeout=90)

    print()
    if response.status_code == 200:
        print("PUT Method Successful.")
        print("----------"*5)
        data = response.json()
        print(data)

    # PATCH request
    json_data = {
        "id": 1,
        "body": "Python requests module to make HTTP requests."
    }

    response = requests.patch(API_URL + "/1", headers=headers, json=json_data, timeout=90)

    print()
    if response.status_code == 200:
        print("PATCH Method Successful.")
        print("----------"*5)
        data = response.json()
        print(data)

    # DELETE request
    response = requests.delete(API_URL + "/1", headers=headers, json=json_data, timeout=90)

    print()
    if response.status_code == 200:
        print("DELETE Method Successful.")
        print("----------"*5)
        data = response.json()
        print(data)
