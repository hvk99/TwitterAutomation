import os
from pathlib import Path
from datetime import datetime

log_path = os.getenv("LOG_PATH")
log_path = "TwitterAutomation.log"


def print_log(message):

    with open(log_path, "a") as f:
        time_now = datetime.now().strftime("%d-%m-%Y.%H-%M-%S")
        f.write(f"{time_now}\t{message}\n")


def print_decorative_log(message):

    with open(log_path, "a") as f:
        time_now = datetime.now().strftime("%d-%m-%Y.%H-%M-%S")
        surround = "=" * 20
        f.write(f"{time_now}\t{surround}{message}{surround}\n")
