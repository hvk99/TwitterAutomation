import os
from pathlib import Path
from dotenv import load_dotenv
import time

load_dotenv(dotenv_path=Path(".env"))

from gemini_prompter import get_content_using_AI
from log_printer import print_decorative_log, print_log
from selenium_driver import get_driver
from twitter_action import login, post_content


def long_sleep(mins):
    for m in range(mins):
        print_log(f"Next post in {mins-m} mins.")
        time.sleep(60)


username = os.getenv("TWITTER_USERNAME")
password = os.getenv("TWITTER_PASSWORD")

print_decorative_log("Starting New Run")
driver = get_driver("https://x.com")

print_log("Sleeping for 2 seconds")
time.sleep(2)

print_log("Starting login process now...")
login(driver, username, password)

for i in range(1, int(os.getenv("NUM_OF_POSTS")) + 1):
    content = get_content_using_AI()
    post_content(driver, content)
    print_log(f"Post {i} out of 10 posted.")
    long_sleep(60)

print_log("Closing the session and the browser")
driver.quit()

print_decorative_log("THE END")
