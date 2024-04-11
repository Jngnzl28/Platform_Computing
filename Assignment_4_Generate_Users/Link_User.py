from selenium import webdriver
from selenium.webdriver.common.by import By
import collections
import csv
import time




def clickLink(driver, reward_time):
    count = -1
    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:
        link.click()
        count += 1
    reward_time += reward_time*count
    return reward_time

def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:3000/")
    reward_time = 10
    total_reward_time = 0
    #total_reward_time = userAction("KEYWORD", driver, reward_time, ["sports", "games"])
    #tag_name = ["img"]
    #total_reward_time += userAction("IMAGE", driver, reward_time, tag_name)
    total_reward_time += clickLink(driver, reward_time)
    time.sleep(10)
    driver.quit()

    print("Presence Time: ", total_reward_time)

if __name__ == "__main__":
    main()