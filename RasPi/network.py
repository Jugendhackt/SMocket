import socket
import subprocess
import sys
from datetime import datetime


def recognize():
    len = 0
    string = str("wlan0")
    out = str(subprocess.check_output(["iw", "dev", "wlan0", "station", "dump"], shell=False)).split("seconds")
    if out == "":
        value = 0
    for i in out:
        if i.find(string) > -1:
            len = len + 1
    if len >= 1:
        value = 1
    else:
        value = 0

    return value
