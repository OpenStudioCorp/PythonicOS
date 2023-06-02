import os
import sys
import time
import subprocess
import socket

from thatonewifi import pydata1,pydata2,pydata3,pydata4,pydata5,pydata6,pydata7,pydata8,pydata9,pydata10
import platform
# def main():
#     if platform.system == 'windows':
#       os.system('cmd /c "python pip install -r requirements.txt"')
#       os.system('cmd /c "python VirtualSerialPorts -l 100"')
    
#     if platform.system == 'linux':
#         os.system('bash "python3 pip install -r requirements.txt"')
#         os.system('bash"python3 VirtualSerialPorts -l 100"')
#         startSH()
        

message = 'Hello, script!'
wait1.send(message.encode())
data = wait2.recv(1024)
print('Received:', data.decode())

def startcmd():
    subprocess.run(["python3", "shell.py"])
    


def timeis():
    secconds = time.time()
    
    
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
    sys.stdout.write('\n')

def startSH():
     print_slow('########  ##    ## ######## ##     ##  #######  ##    ## ####  ######                #######   ######  ')
     print_slow('##     ##  ##  ##     ##    ##     ## ##     ## ###   ##  ##  ##    ##              ##     ## ##    ## ')
     print_slow('##     ##   ####      ##    ##     ## ##     ## ####  ##  ##  ##       -#-#-#-#-#-  ##     ## ##       ')
     print_slow('########     ##       ##    ######### ##     ## ## ## ##  ##  ##       #-#-#-#-#-#  ##     ##  ######  ')
     print_slow('##           ##       ##    ##     ## ##     ## ##  ####  ##  ##       -#-#-#-#-#-  ##     ##       ## ')
     print_slow('##           ##       ##    ##     ## ##     ## ##   ###  ##  ##    ##              ##     ## ##    ## ')
     print_slow('##           ##       ##    ##     ##  #######  ##    ## ####  ######                #######   ######  ')
     print_slow('*******************************************************************************************************')
     print_slow('-------------------------------------------PythonicOS--------------------------------------------------')
     print_slow('-------------------------------------------version 1.0-------------------------------------------------')
     print_slow('-----------------------copywrite 2023 OpenStudio and the amazing github suporters----------------------')
     print_slow('------------------welcome to the interactive start wizard for Windows, MacOS and Linux.----------------')
     print_slow('-------------------------------------------------------------------------------------------------------')
     print_slow('-------------------this wizard will allow you to navagate PythonicOS and its features!-----------------')
     print_slow('---------------using the helpfull commands listed below you can nvagate around the shell!--------------')
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
