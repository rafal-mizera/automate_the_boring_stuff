import os
import requests
import threading
import bs4

os.makedirs("xkcd",exist_ok=True)

def download_xkcd(start_comic, end_comic):
    for url_nr in range(start_comic,end_comic):
        print("Downloading the page...")
        res = requests.get(f"http://xkcd.com/{url_nr}")
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text,features="html.parser")

        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find the comic image...")
        else:
            comic_url = "http:" + comic_elem[0].get("src")
            print(comic_url)
            print("Downloading the image...")
            res = requests.get(comic_url)
            res.raise_for_status()

            with open(os.path.join("xkcd",os.path.basename(comic_url)),"wb") as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)

download_threads = []
for i in range(1,1400,100):
    download_thread = threading.Thread(target=download_xkcd,args=(i,i+99))
    download_threads.append(download_thread)
    download_thread.start()

#wait for all threads to end
for thread in download_threads:
    thread.join()
print("Done")
