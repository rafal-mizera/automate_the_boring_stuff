import requests

# res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# type(res)
#
#
# res.status_code == requests.codes.ok
#
# len(res.text)

# print(res.text[:2500])
####################################################################################################
# res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print(f"Oops... Something's gone wrong... {exc}")
####################################################################################################
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)