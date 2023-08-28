import os
import subprocess
import tkinter
from tkinter import messagebox
import shutil


def print_greetings():
    '''
    Print a welcome message to the user.
    '''
    print("Welcome to PythonicOS!")
    print("Version 1.0")


def print_help():
    print("Here are the available commands:")
    print("cd <directory>: Change current working directory to <directory>")
    print("help: Display this help message")
    print("exit: Exit PythonicOS")
    print("mkdir: Create a new directory")
    print("editfile: Edit a file")
    print("senddata: Send data to the other computer")
    print("ls: List the contents of the current working directory")
    print("rm: Remove a file")
    print("rmdir: Remove a directory")
    print("mv: Move a file or directory")

def cd():
    '''
    Change the current working directory.
    '''
    directory_name = input("Enter the name of the directory to change to: ")
    path = os.path.join(os.getcwd(), directory_name)
    if not os.path.exists(path):
        print("Directory '%s' does not exist." % directory_name)
        return

    try:
        os.chdir(path)
        print("Current working directory changed to '%s'." % directory_name)
    except OSError as error:
        print("Error changing directory '%s': %s" % (directory_name, error))

def mkdir():
    '''
    Create a new directory in the current working directory.
    '''
    directory_name = input("Enter the name of the directory to be created: ")
    path = os.path.join(os.getcwd(), directory_name)

    try:
        os.mkdir(path)
        print("Directory '%s' created successfully." % directory_name)
    except OSError as error:
        print("Error creating directory '%s': %s" % (directory_name, error))


def editfile():
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
        print("Error editing file '%s': %s" % (filename, error))


def senddata():
    print('hallo! sorry for the inconvenience, but this feature is not yet implemented. it used to be but it was removed because it was not working properly.')


def StartOS():
    subprocess.Popen(['python', 'PythonicOS.py']) # pass the command as a list of strings
    # OHHHH MYYYY FFFFFFFFFUUUUUUUUUUUUUUU- DAMMMITTTTT -charlie
def ls():
    '''
    List the contents of the current working directory.
    '''
    print(os.listdir(os.getcwd()))
def rm():
    '''
    Remove a file in the current working directory.
    '''
    filename = input("Enter the name of the file to remove: ")
    path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(path):
        print("File '%s' does not exist." % filename)
        return

    try:
        os.remove(path)
        print("File '%s' removed successfully." % filename)
    except OSError as error:
        print("Error removing file '%s': %s" % (filename, error))

def rmdir():
    '''
    Remove a directory in the current working directory.
    '''
    directory_name = input("Enter the name of the directory to remove: ")
    path = os.path.join(os.getcwd(), directory_name)
    if not os.path.exists(path):
        print("Directory '%s' does not exist." % directory_name)
        return

    try:
        os.rmdir(path)
        print("Directory '%s' removed successfully." % directory_name)
    except OSError as error:
        print("Error removing directory '%s': %s" % (directory_name, error))

def mv():
    '''
    Move a file or directory in the current working directory.
    '''
    source = input("Enter the name of the file or directory to move: ")
    destination = input("Enter the name of the destination: ")
    source_path = os.path.join(os.getcwd(), source)
    destination_path = os.path.join(os.getcwd(), destination)
    if not os.path.exists(source_path):
        print("File or directory '%s' does not exist." % source)
        return

    try:
        os.rename(source_path, destination_path)
        print("File or directory '%s' moved successfully." % source)
    except OSError as error:
        print("Error moving file or directory '%s': %s" % (source, error))

def cp():
    '''
    Copy a file or directory in the current working directory.
    '''
    source = input("Enter the name of the file or directory to copy: ")
    destination = input("Enter the name of the destination: ")
    source_path = os.path.join(os.getcwd(), source)
    destination_path = os.path.join(os.getcwd(), destination)
    if not os.path.exists(source_path):
        print("File or directory '%s' does not exist." % source)
        return

    try:
        shutil.copy(source_path, destination_path)
        print("File or directory '%s' copied successfully." % source)
    except OSError as error:
        print("Error copying file or directory '%s': %s" % (source, error))

def touch():
    '''
    Create a new file in the current working directory.
    '''
    filename = input("Enter the name of the file to create: ")
    path = os.path.join(os.getcwd(), filename)

    try:
        open(path, 'a').close()
        print("File '%s' created successfully." % filename)
    except OSError as error:
        print("Error creating file '%s': %s" % (filename, error))

def cat():
    '''
    Display the contents of a file in the current working directory.
    '''
    filename = input("Enter the name of the file to display: ")
    path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(path):
        print("File '%s' does not exist." % filename)
        return

    try:
        with open(path, 'r') as file:
            print(file.read())
    except OSError as error:
        print("Error displaying file '%s': %s" % (filename, error))

def pwd():
    '''
    Print the current working directory.
    '''
    print(os.getcwd())
    
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def monty():
    subprocess.Popen(['python', './python/system/addons/montyai.py'])

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
        elif tokens[0] == "cls":
            cls()
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
        elif tokens[0] == "ls":
            ls()
        elif tokens[0] == "rm":
            rm()
        elif tokens[0] == "rmdir":
            rmdir()
        elif tokens[0] == "pwd":
            pwd()
        elif tokens[0] == "cp":
            cp()
        elif tokens[0] == "cat":
            cat()
        elif tokens[0] == "monty":
            monty()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()
        # elif tokens[0] == "rmdir":
        #     rmdir()

        elif tokens[0] == "time":
            subprocess.call(['python', './python/time.py'])
        elif tokens[0] == "date":
            subprocess.Popen(['python', './python/time.py'])
        else:
            print(f"{tokens[0]}: command not found")


if __name__ == "__main__":
    my_shell()
    input("Press Enter to exit...")
