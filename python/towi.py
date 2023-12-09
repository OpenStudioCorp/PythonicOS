import urllib.request
import urllib.parse
import json
import re
import requests
import math
import pickle
import threading
import traceback
import logging
import glob
import websocket
import os
import time
import sys
import random
import datetime
import shutil
import subprocess
import platform
import getpass

###########
# the wifi module for PythonicOS
###########


def websocket(url, message):
    # Websocket
    ws = websocket.WebSocket()
    ws.connect(url)
    ws.send(message)
    result = ws.recv()
    ws.close()
    return result
    
def internet(link):
    # Check if there is internet
    try:
        urllib.request.urlopen(link, timeout=1)
        return True
    except urllib.request.URLError as err:
        return False
    
def ping(host):
    # Ping a host
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0
