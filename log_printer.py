import os
from pathlib import Path

def print_log(message):

    with open(r"D:\CS\Python\Automate Everything with Python\Twitter Automation\run.log", "a") as f:
        time_now = datetime.now().strftime("%d-%m-%Y.%H-%M-%S")
        f.write(f"{time_now}\t{message}\n")


def print_decorative_log(message):

    with open(r"D:\CS\Python\Automate Everything with Python\Twitter Automation\run.log", "a") as f:
        time_now = datetime.now().strftime("%d-%m-%Y.%H-%M-%S")
        surround = "=" * 20
        f.write(f"{time_now}\t{surround}{message}{surround}\n")