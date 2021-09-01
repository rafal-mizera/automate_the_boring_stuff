import requests
import os
import bs4


os.makedirs("top_500_posters",exist_ok=True)

url = "https://www.filmweb.pl/ranking/film"
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")
movies_links = soup.select(".rankingType__title a")
print(len(movies_links))
# for i in range(20):
#     link = "https://www.filmweb.pl" + movies_links[i].get("href")
#     res = requests.get(link)
#     res.raise_for_status()
#     soup = bs4.BeautifulSoup(res.text,"html.parser")
#     posters_link = soup.select(".filmPosterSection__poster a img")
#     poster = posters_link[0].get("content")
#
#     poster_res = requests.get(poster)
#     poster_res.raise_for_status()
#
#     with open(os.path.join("top_500_posters",os.path.basename(poster)),"wb") as posterFile:
#         for chunk in poster_res.iter_content(100000):
#             posterFile.write(chunk)
#             print(f"{os.path.basename(poster)} saved to top_500_posters")
#
# print("Done :)")
