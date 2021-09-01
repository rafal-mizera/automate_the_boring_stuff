from selenium import webdriver


# browser = webdriver.Firefox()
#
# print(type(browser))
#
# browser.get("http://inventwithpython.com")
#
# try:
#     link_elem = browser.find_element_by_link_text('Read Online for Free')
#     print('Found <%s> element!' % (link_elem.tag_name))
#     link_elem.click()
# except:
#     print('Was not able to find an element with that name.')

#############################################################################3
# browser = webdriver.Firefox()
# browser.get("http://gmail.com")
#
# emailElem = browser.find_element_by_id("identifierId")
# emailElem.send_keys("some_fake_email@gmail.com")
# nextELem = browser.find_element_by_css_selector(".VfPpkd-RLmnJb")
# nextELem.click()
###############################################################################3
from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()
# browser.get('http://nostarch.com')
# htmlElem = browser.find_element_by_tag_name('html')
# htmlElem.send_keys(Keys.END) # scrolls to bottom
# htmlElem.send_keys(Keys.HOME) # scrolls to top
#################################################################################3




