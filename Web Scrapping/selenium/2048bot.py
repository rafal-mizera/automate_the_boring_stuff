"""opens https://gabrielecirulli.github.io/2048/ - a site with 2048 game and plays the game repeatedly using up, right,
down and left arrows"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

game_url = "https://gabrielecirulli.github.io/2048/"

browser = webdriver.Firefox()
browser.get(game_url)
scores = []
start = time.time()
try:
    while len(scores) < 3:
        try:
            retryEl = browser.find_element_by_link_text("Try again")
            score = browser.find_element_by_css_selector(".score-container")
            scores.append(score.text)
            retryEl.click()

        except Exception:
            htmlEl = browser.find_element_by_tag_name("html")
            htmlEl.send_keys(Keys.ARROW_UP)
            htmlEl.send_keys(Keys.ARROW_RIGHT)
            htmlEl.send_keys(Keys.ARROW_DOWN)
            htmlEl.send_keys(Keys.ARROW_LEFT)

    stop = time.time()
    browser.close()
    time = stop - start
    print(f"Czas trwania programu: {time:.2f} s")
    print("Najlepsze wyniki:")
    i = 1
    for score in sorted(scores):
        print(f"{i}. miejsce - {score}")
        i += 1

except Exception:
    print("Program został zamknięty...")


