import bs4
import requests

# res = requests.get("http://nostarch.com")
# res.raise_for_status()
#
# noStarchSoup = bs4.BeautifulSoup(res.text,features="html.parser")
# print(type(noStarchSoup))

exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(),features="html.parser")

# elems = exampleSoup.select("#author")
# print(type(elems))
# print(elems)
# print(len(elems))
# print(elems[0])
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)
#
# pElems = exampleSoup.select("p")
# print(len(pElems))
# print(pElems[0])
# print(pElems[0].getText())

soup = bs4.BeautifulSoup(exampleFile,features="html.parser")
spanElem = soup.select("span")[0]
print(spanElem)
print(str(spanElem))
print(spanElem.get("id"))
print(spanElem.attrs)
