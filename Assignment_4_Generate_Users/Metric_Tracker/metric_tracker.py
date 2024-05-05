import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import collections
from Unique_User import userAction

uri = "mongodb+srv://jngnzles:Krom484Devi@cluster0.9wfdlln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client.your_database

def main():

    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")
    metrics = collections.defaultdict()
    print("HERE")
    start_time = time.time()

    presence_time = start_time
    userAction(driver)
    current_time = time.time()

    presence_time = current_time - start_time
    print(f"Presence time: {presence_time} seconds")
    metrics[str(current_time)+" Presence time (seconds)"] = presence_time

    driver.quit()

if __name__ == "__main__":
    main()