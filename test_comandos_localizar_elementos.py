import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://www.saucedemo.com/")

# find_element()

username = browser.find_element(By.ID, "user-name")
password = browser.find_element(By.ID, "password")
btn_login = browser.find_element(By.ID, "login-button")

# send_keys()
username.send_keys("standard_user")
password.send_keys("secret_sauce")

# click()

btn_login.click()

# text

products_titles = browser.find_elements(By.XPATH, "//span[@class='title']")

for title in products_titles:
    print(title.text)
    assert title.text == "Products"

# get_attribute()
img_backpack = browser.find_element(By.XPATH, "//*[@id='item_4_img_link']/img")
alt_attribute = img_backpack.get_attribute("alt")

print(alt_attribute)
assert alt_attribute == "Sauce Labs Backpack"