"""Learning about the Multiprocessing in Python"""

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import requests
import time

def download_image(url, name):
    """Function to download an image."""

    print(f"Downloading an Image {name}")
    response = requests.get(url, timeout=60)

    if response.status_code == 200:
        with open(f"./Python/images/{name}.jpg", "wb") as file:
            file.write(response.content)
     
    print(f"Finished Downloading an Image {name}")


url = "https://picsum.photos/5000/3000"


if __name__ == "__main__":

    print("\nProcess without Multiprocessing")
    print("----------"*10)
    start_time = time.perf_counter()

    for _ in range(1, 21):
        download_image(url, _)

    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")


    print("\nProcess with Multiprocessing")
    print("----------"*10)
    start_time = time.perf_counter()
    processes = []

    for _ in range(1, 21):
        p = multiprocessing.Process(target=download_image, args=(url, _))
        p.start()
        processes.append(p)

    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")

    print("\nProcess with Process Pool")
    print("----------"*10)
    start_time = time.perf_counter()

    args = [ _ for _ in range(1, 21)]
    urls = [url for _ in range(20)]

    with ProcessPoolExecutor() as executor:
        results = executor.map(download_image, urls, args)

    print(f"Time taken to execute the tasks : {time.perf_counter() - start_time} seconds\n")

    for p in processes:
        p.join()
    