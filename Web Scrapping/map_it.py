import webbrowser
import pyperclip
import sys

"""Launches browser with google maps and goes to map of given address"""
# webbrowser.open('http://inventwithpython.com/')

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
#     address = pyperclip.paste()
    country = input("Please input country name: ")
    state = input("Please input state: ")
    city = input("Please input city name: ")
    street = input("Please input street name: ")
    street_nr = input("Please input street nr: ")
    address = f"{street} {street_nr}, {city}, {state}, {country}"

webbrowser.open(f"http://google.com/maps/place/{address}")


# 870 Valencia St, San Francisco, CA 94110

