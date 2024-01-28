"""Learning about the Multithreading in Python"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor
import requests


def download_image():
    """Function to download an image."""

    print("Downloading an Image")
    time.sleep(2)
    image_url = "https://blogger.googleusercontent.com/img/a/AVvXsEhqzeTOTJm2J-wrSe9kAj3DlAphY5RzFw3W4xf25OPT1AEktfD1Z70sYBclrMDeuD6jAeZzJPByXgH272iG3hxS7AGppznCwS1yzioR77m4J03rVdFLmL3TtLjVmUfaCk-p1D3Jdkj6fp-9U64Tnqg1EMKT9OXpclfVjKrYeqT-OJWdnq9JBh_8ZZKWpsM=w640-h360"

    response = requests.get(image_url, timeout=60)

    if response.status_code == 200:
        with open("./Python/images/image.jpg", "wb") as file:
            file.write(response.content)
            
    print("Finished downloading an Image")


def fetch_data():
    """Function to fetch data from REST API"""

    print("Fetching the Data")
    time.sleep(2)
    api_url = "https://dummyjson.com/products"

    response = requests.get(api_url, timeout=60)

    if response.status_code == 200:
        products = response.json()["products"]

        rows = []
        for product in products:
            row = f"{product['id']},{product['title']},{product['description']},{product['stock']}\n"
            rows.append(row)

        with open("./Python/images/products.csv", "w", encoding="utf-8") as file:
            file.writelines(rows)
            
        print("Finished fetching the data")

def main():
    """Basic Multithreading"""

    print("\nProcess without Multithreading")
    print("----------"*10)
    start_time = time.perf_counter()
    download_image()
    fetch_data()
    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")


    print("\nProcess with Multithreading")
    print("----------"*10)
    start_time = time.perf_counter()
    t1 = threading.Thread(target=download_image)
    t2 = threading.Thread(target=fetch_data)

    t1.start()
    t2.start()

    # Waiting for the threads to complete tasks
    t1.join()
    t2.join()

    # We will get time taken by longest process
    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")

    # Multithreading using Thread Pool
    print("\nProcess with ThreadPool")
    print("----------"*10)

    start_time = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        t1 = executor.submit(download_image)
        t2 = executor.submit(fetch_data)

    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")

if __name__ == "__main__":
    main()