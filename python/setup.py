import os
import sys
import datetime

DIRS = [
    'home',
    'bin',
    'scripts',
    'addons',
    'documents',
    'home/user',
    'home/user/documents',
    'home/user/documents/projects',
    'system',
    'system/scripts',
    'system/logs'
    'mount'
]

def main():
    for i in DIRS:
        if not os.path.exists(i):
            os.makedirs(i)
