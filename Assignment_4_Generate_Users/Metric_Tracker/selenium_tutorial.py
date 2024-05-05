# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# starts session
driver = webdriver.Chrome()

# navigates the browser
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# requests browser information
title = driver.title

# waiting strategy
driver.implicitly_wait(20)

# finds the element
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# takes action on an element
text_box.send_keys("Selenium")
submit_button.click()

# finds the element with the value messsage
message = driver.find_element(by=By.ID, value="message")

# elements store a lot of information that can be requested.
text = message.text

# prvents webpage from closing prematurely (c)
while True:
    print()

# ends the session
driver.quit()