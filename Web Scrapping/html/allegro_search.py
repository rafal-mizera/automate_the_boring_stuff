import requests
import webbrowser
import bs4

searched_item = input("Wpisz nazwę poszukiwanego przedmiotu: ")

res = requests.get(f"https://allegro.pl/listing?string={searched_item}")
soup = bs4.BeautifulSoup(res.text,"html.parser")

links = soup.select("div.opbox-listing a")

opened = []
for i in range(3):
    link = links[i].get("href")
    if link in opened:
       link = links[i+2].get("href")
    webbrowser.open(link)
    opened.append(link)
    print(opened)

