"""Prints the weather for the location from users input"""

import json
import requests
from collections import namedtuple

location = input("Please input location: ")
Weather = namedtuple("Weather", ["the_temp", "air_pressure", "humidity"])

def get_location_id(location):
    resp = requests.get(f"https://www.metaweather.com/api/location/search/?query={location}")
    woeid = resp.json()[0]["woeid"]
    return woeid

def get_location_weather(woeid):
    resp = requests.get(f"https://www.metaweather.com/api/location/{woeid}/")
    w = resp.json()['consolidated_weather'][0]
    weather = Weather(w['the_temp'],w['air_pressure'],w['humidity'])
    return weather

def report(w, location_name):
    rep = f"Pogoada w {location_name}\n"
    rep += f"Temperatura: {w.the_temp:.1f} stopni Celsjusza\n"
    rep += f"Wilgotność: {w.humidity} %\n"
    rep += f"Ciśnienie: {w.air_pressure} hPa\n"
    return rep

if __name__ == "__main__":
    location_id = get_location_id(location)
    weather = get_location_weather(location_id)
    rep = report(weather, location)
    print(rep)





