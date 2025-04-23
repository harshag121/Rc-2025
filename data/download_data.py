import os
import urllib.request
import zipfile


def download_movielens():
    datasets = [
        ("ml-100k", "https://files.grouplens.org/datasets/movielens/ml-100k.zip"),
        ("ml-25m", "https://files.grouplens.org/datasets/movielens/ml-25m.zip"),
    ]
    for folder, url in datasets:
        zip_name = f"{folder}.zip"
        if not os.path.exists(folder):
            print(f"Downloading {folder}...")
            urllib.request.urlretrieve(url, zip_name)
            with zipfile.ZipFile(zip_name, 'r') as z:
                z.extractall()
            print(f"{folder} downloaded and extracted.")
        else:
            print(f"{folder} already exists, skipping.")

if __name__ == '__main__':
    download_movielens()