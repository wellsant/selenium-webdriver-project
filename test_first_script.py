import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://google.com")
time.sleep(6)
browser.quit()

