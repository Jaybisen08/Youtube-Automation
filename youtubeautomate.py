from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
sleep(3)
browser.get("https://youtube.com")
sleep(3)
search_box = browser.find_element("name", "search_query")
for char in "indian veg food":
    search_box.send_keys(char)
    sleep(0.2)
sleep(6)
search_box.send_keys(Keys.ENTER)
sleep(3)
first_short = browser.find_element("xpath",'//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div[1]')
first_short.click()

while True:
    sleep(10)
    next_button = browser.find_element("xpath", '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
    next_button.click()
 
