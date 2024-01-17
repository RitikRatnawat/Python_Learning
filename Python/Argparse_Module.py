"""Learning about the Argument parser in the Python by creating a Command Line Utility."""

import os
import argparse
import requests

# Creating a Parser Object
parser = argparse.ArgumentParser()

# Adding parser arguments to the command line utility
parser.add_argument("-u", "--url", help="URL of the file to download")
parser.add_argument("-o", "--output", help="Name of the file", default=None)

def download_file(url, filename):
    """Function to download a file using requests

    Args:
        url (str): URL of the file to download
        filename (str): Name of the File to be saved as

    Returns:
        str : Name of the File
    """

    if not filename:
        filename = os.path.join("images", url.split("/")[-1])
    else:
        filename = os.path.join("images", filename)

    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return filename


if __name__ == "__main__":

    # Parse the Arguments
    args = parser.parse_args()

    # Downloading a File
    file = download_file(args.url, args.output)
    print(f"File downloaded at : {os.path.realpath(file)}")
