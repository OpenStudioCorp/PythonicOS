import os
import subprocess
from python.towii import pydata1,pydata2

import tkinter
from tkinter import messagebox
from file import home_dir,config_file,addons,usrpass,pythonOS

def print_greetings():
    
    print("thanks for using PythonicShell!")
    print("Version 1.0")

def print_help():
    print("Here are the available commands:")
    print("cd <directory>: Change current working directory to <directory>")
    print("help: Display this help message")
    print("exit: Exit MyShell")


def mkdir():
    directory_name = input("Enter the name of the directory to be created: ")
    path = os.path.join(os.getcwd(), directory_name)

    try:
        os.mkdir(path)
        print("Directory '%s' created successfully." % directory_name)
    except OSError as error:
        print("Error creating directory '%s': %s" % (directory_name, error))
def editfile():
    filename = input("Enter the name of the file to edit: ")
    path = os.path.join(os.getcwd(), filename)
    if 'path' == None:
        open(filename, 'w')

    if not 'path' == None:
        try:
            subprocess.run(["nano", path])
            print("editing file!", filename)
        except OSError as error:
            print("Error editing file '%s': %s" % (filename, error))
def senddata():
    message = input()
    pydata1.send(message.encode())
def StartOS():
    subprocess.Popen('PythonicOS.exe')

def my_shell():
    print_greetings()

while True:
    command = input(f"{os.getcwd()} $ ")
    tokens = command.split()

    if len(tokens) == 0:
        continue
    if tokens[0] == "cd":
        if len(tokens) > 1:
            os.chdir(tokens[1])
        else:
            print("cd: missing operand")
    elif tokens[0] == "help":
        print_help()
    elif tokens[0] == "sd":
        senddata()
    elif tokens[0] == "exit":
        break
    elif tokens[0] == "help":    
        print_greetings()
    elif tokens[0] == "edit":    
        editfile()
    elif tokens[0] == "start":
        StartOS()

    else:
        print(f"{tokens[0]}: command not found")

if __name__ == "__main__":
    my_shell()
    input("Press Enter to exit...")
