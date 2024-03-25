import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerAPI
import collections

uri = "mongodb+srv://jngnzles:Krom484Devi@cluster0.9wfdlln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client.your_database

def main():

    # Initialize browser
    driver = webdriver.Chrome()

    # Navigate to your website 
    driver.get("http://localhost:3000/")

    # Initialize variables
    metrics = []
    SAMPLE_SIZE = 2
    count = 0
    start_time = time.time()
    presence_time = start_time

    while count < SAMPLE_SIZE:
        # Track presence time
        current_time = time.time()
        presence_time = current_time - start_time
        print(f"Presence time: {presence_time} seconds")
    
        # Track scrolling
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        current_scroll = driver.execute_script("return window.pageYOffset")
        print(f"Scrolled {current_scroll}/{scroll_height} pixels")

        metrics.append({"TIMESTAMP (HH:MM:SS)": time.strftime("%H:%M:%S", time.localtime()),
                        "Presence time (Seconds)" : presence_time,
                        "Scrolling (Pixels)" : current_scroll/scroll_height})
        db.collection.insert_many(metrics)
        count += 1
        time.sleep(2)
    
    print(metrics)

if __name__ == "__main__":
    main()


# Track presence time 
# start_time = time.time()
# presence_time = start_time
# while True:#presence_time < 50: # seconds
#    current_time = time.time()
#    presence_time = current_time - start_time
#     print(f"Presence time: {presence_time} seconds")
    
#     # Track scrolling
#     scroll_height = driver.execute_script("return document.body.scrollHeight")  
#     current_scroll = driver.execute_script("return window.pageYOffset")
#     print(f"Scrolled {current_scroll}/{scroll_height} pixels")