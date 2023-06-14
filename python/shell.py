import os
import subprocess
import tkinter
from tkinter import messagebox
from towii import pydata1, pydata2


def print_greetings():
    '''
    Print a welcome message to the user.
    '''
    print("Thanks for using PythonicShell!")
    print("Version 1.0")


def print_help():
    print("Here are the available commands:")
    print("cd <directory>: Change current working directory to <directory>")
    print("help: Display this help message")
    print("exit: Exit MyShell")


def mkdir():
    '''
    Create a new directory in the current working directory.
    '''
    directory_name = input("Enter the name of the directory to be created: ")
    path = os.path.join(os.getcwd(), directory_name)

    try:
        os.mkdir(path)
        print(f"Directory '{directory_name}' created successfully.")
    except OSError as error:
        print(f"Error creating directory '{directory_name}': {error}")


def editfile():
    # If you're just gonna use nano anyway, why even bother having this?
    '''
    Edit a file in the current working directory.
    '''
    filename = input("Enter the name of the file to edit: ")
    path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(path):
        open(filename, 'w')

    try:
        subprocess.run(["nano", path])
        print("Editing file:", filename)
    except OSError as error:
        print(f"Error editing file '{filename}': {error}")


def senddata():
    message = input("Enter the message to send: ")
    pydata1.send(message.encode('utf-8'))


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
        elif tokens[0] == "time":
            subprocess.call(['python', 'python/time.py'])
        else:
            print(f"{tokens[0]}: command not found")


if __name__ == "__main__":
    my_shell()
    input("Press Enter to exit...")
