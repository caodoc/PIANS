import urllib.request
import os

def Get(path, container):
    with open(path, "r") as file:
        list = file.read().splitlines()
    
    cnt = 0
    name = ""
    for link in list:
        try:
            cnt += 1
            name = str(cnt) + ".png"
            download_path = os.path.join(container, name)
            urllib.request.urlretrieve(link, download_path)
            print(f"Downloaded: {link}")
        except Exception as e:
            print(f"Failed to download: {link}")
            print(f"Error: {str(e)}")

file = "1659341999.txt"

folder = "./Hina"

Get(file, folder)