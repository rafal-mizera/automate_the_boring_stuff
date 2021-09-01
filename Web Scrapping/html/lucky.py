#! python3
# lucky.py - Opens several Google search results.

import requests
import webbrowser
import bs4
import sys

print('Googling...') # display text while downloading the google page
# searched = sys.argv[1:]
searched = "polska"
res = requests.get(f"http://www.google.com/search?q={searched}")
# res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,features="html.parser")
links_to_open = soup.select('div#main > div > div > div > a')


print(links_to_open)

numOpen = min(5,len(links_to_open))

for i in range(numOpen):
    webbrowser.open("google.com" + links_to_open[i].get("href"))




