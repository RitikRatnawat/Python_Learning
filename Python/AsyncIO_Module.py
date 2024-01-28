"""Learning about the AsyncIO module in Python"""

import asyncio
import requests


async def download_image():
    """Function to download an image."""

    print("Downloading an Image")
    await asyncio.sleep(5)
    image_url = "https://blogger.googleusercontent.com/img/a/AVvXsEhqzeTOTJm2J-wrSe9kAj3DlAphY5RzFw3W4xf25OPT1AEktfD1Z70sYBclrMDeuD6jAeZzJPByXgH272iG3hxS7AGppznCwS1yzioR77m4J03rVdFLmL3TtLjVmUfaCk-p1D3Jdkj6fp-9U64Tnqg1EMKT9OXpclfVjKrYeqT-OJWdnq9JBh_8ZZKWpsM=w640-h360"

    response = requests.get(image_url, timeout=60)

    if response.status_code == 200:
        with open("./Python/images/image.jpg", "wb") as file:
            file.write(response.content)


async def fetch_data():
    """Function to fetch data from REST API"""

    print("Fetching the Data")
    await asyncio.sleep(2)
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



async def main():
    """Main Function"""

    # Creating Asynchronous Tasks
    # task1 = asyncio.create_task(download_image())
    # task2 = asyncio.create_task(fetch_data())

    # Running tasks Parallely
    await asyncio.gather(
        download_image(),
        fetch_data()
    )

asyncio.run(main())
