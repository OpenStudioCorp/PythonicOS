import os
import sys
import time
import subprocess
import platform
from towii import pydata1, pydata2,time1

def startcmd():
        subprocess.call('shell.exe',)

def timeis():
    secconds = time.time()
    time1.sendall(secconds)
    
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\n')

def startSH():
    pydata1.sendall(b"Hello! just letting you know that PythonicOS is starting!")
    data = pydata2.recv(1024)
    print("Received:", data.decode())
    print_slow('########  ##    ## ######## ##     ##  #######  ##    ## ####  ######                #######   ######  ')
    print_slow('##     ##  ##  ##     ##    ##     ## ##     ## ###   ##  ##  ##    ##              ##     ## ##    ## ')
    print_slow('##     ##   ####      ##    ##     ## ##     ## ####  ##  ##  ##       -#-#-#-#-#-  ##     ## ##       ')
    print_slow('########     ##       ##    ######### ##     ## ## ## ##  ##  ##       #-#-#-#-#-#  ##     ##  ######  ')
    print_slow('##           ##       ##    ##     ## ##     ## ##  ####  ##  ##       -#-#-#-#-#-  ##     ##       ## ')
    print_slow('##           ##       ##    ##     ## ##     ## ##   ###  ##  ##    ##              ##     ## ##    ## ')
    print_slow('##           ##       ##    ##     ##  #######  ##    ## ####  ######                #######   ######  ')
    print_slow('*******************************************************************************************************')
    print_slow('-------------------------------------------PythonicOS--------------------------------------------------')
    print_slow('---------------------------------------------v 0.1-----------------------------------------------------')
    print_slow('------------------Copyright 2023 OpenStudio and our github supporters and collaborators----------------')
    print_slow('------------------Welcome to the interactive start wizard for Windows, MacOS and Linux.----------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-------------------This wizard will allow you to navagate PythonicOS and its features!-----------------')
    print_slow('----------------using the helpful commands listed below you can navigate around the shell!-------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-----------------------------------CD <directory>: changes directory-----------------------------------')
    print_slow('-------------------MKDIR followed by <directoryname> on a new line: makes a directory------------------')
    print_slow('------------------------------------------Help: displays Help------------------------------------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('-------------------------------------------------------------------------------------------------------')
    print_slow('*******************************************************************************************************')
    startcmd()
if __name__ == ('__main__'):
    startSH()
