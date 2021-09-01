"Opens web browser ands sends email/emails to given address/addresses"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

message = input("Please write your message:\n")
topic = input("Please write email topic:\n")
email = input("Please write email address:\n")
password = "Python123"
my_email = "kontodonaukiprogramowania123"

browser = webdriver.Firefox()
browser.get("http://gmail.com")
emailElem = browser.find_element_by_css_selector("#identifierId")
emailElem.send_keys(my_email)
nextElem = browser.find_element_by_css_selector(".VfPpkd-RLmnJb")
nextElem.click()
time.sleep(5)
passElem = browser.find_element_by_css_selector("#password > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
passElem.send_keys(password)
nextElem = browser.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > div:nth-child(3)")
nextElem.click()
time.sleep(5)
newemailEl = browser.find_element_by_css_selector(".T-I-KE")
newemailEl.click()
time.sleep(5)
addressEl = browser.find_element_by_css_selector("#\:80")
addressEl.send_keys(email)
topicEl = browser.find_element_by_css_selector("#\:7i")
topicEl.send_keys(topic)
messageEl = browser.find_element_by_css_selector("#\:8n")
messageEl.send_keys(message)
time.sleep(5)
sendEl = browser.find_element_by_css_selector("#\:78")
sendEl.click()
time.sleep(5)
logout1 = browser.find_element_by_css_selector(".gb_Da")
logout1.click()
time.sleep(5)
logout2 = browser.find_element_by_css_selector("#gb_71")
logout2.click()
browser.close()

print("Your message has been sent :)")
