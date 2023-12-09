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


###########
#modules###
###########

#owi
from towi import websocket, internet,ping
#

#####



def printslow(text):
    for c in text:
        print(c, end='')
        time.sleep(0.05)
        
def printfast(text):
    for c in text:
        print(c, end='')
        time.sleep(0.01)
        


def clear():
    # Clear the screen
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
