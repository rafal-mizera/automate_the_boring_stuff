#! python3
# downloadXKCD.py - Downloads every single XKCD comic.

import requests
import os
import bs4

url = "http://xkcd.com"

os.makedirs("xkcd", exist_ok=True)

#find the url of the image
while not url.endswith("#"):
    res = requests.get(url)
    print("Downloading page...")
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    comic = soup.select("#comic img")
    if comic == []:
        print("Could not find the image...")
    else:
        comic_link = "http:" + comic[0].get("src")
        print(f"Downloading image {comic_link}...")
        res = requests.get(comic_link)
        res.raise_for_status()
        with open(os.path.join("xkcd",os.path.basename(comic_link)),"wb") as ImageFile:
            for chunk in res.iter_content(100000):
                ImageFile.write(chunk)
        prev = soup.select("a[rel= 'prev']")[0]
        url = "http://xkcd.com" + prev.get("href")
        print("Done")








