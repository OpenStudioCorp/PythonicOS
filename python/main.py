#######
# PythonicOS
# Author: charlie-sans from OpenStudioCorp
# Date: 2023
# Description: Main file for the PythonicOS project
#######


###########
##Imports##
###########

import os
import time
import sys
import random
import datetime
import shutil
import subprocess
import platform
import getpass
import socket
import webbrowser
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
###########




def printslow(text):
    for c in text:
        print(c, end='')
        time.sleep(0.05)
        
def printfast(text):
    for c in text:
        print(c, end='')
        time.sleep(0.01)
        

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

def clear():
    # Clear the screen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
def websocket():
    # Websocket

    ws = websocket.WebSocket()
    ws.connect("ws://echo.websocket.org")
    ws.send("Hello, World")
    ws.recv()
    ws.close()