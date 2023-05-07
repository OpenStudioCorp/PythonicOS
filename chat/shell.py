import os
import desktop
from desktop import run_with_panno
from desktop import filepath
import subprocess


def display_greetings():
    print("Welcome to PythonicOS")
    print("Version 1.0\n")

def audioplayer(filepath):
     subprocess.Popen(['python', 'addons/audioplayer.py'], cwd=filepath)
def display_help():
    print("PythonicOS Help")
    print("-------------")
    print("cd <directory>: Changes the current working directory to the specified directory.")
    print("help: Displays this help message.")
    print("exit: Exits MyShell.\n")
    print('mkdir: makes a directory')
    print("panno; creates a file")
    print("mp: opens a music player")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

def start_python_operating_system():
    subprocess.Popen(['python', 'PythonOS.py'], cwd=filepath)


def main():
    display_greetings()

    while True:
        # Get user input
        user_input = input(os.getcwd() + "> ")

        # Split the input into command and arguments
        parts = user_input.split()
        command = parts[0]

        # Execute the command
        if command == "cd":
            if len(parts) > 1:
                os.chdir(parts[1])
            else:
                print("Please specify a directory to change to.")
        elif command == "help":
            display_help()
        elif command == "panno":
            run_with_panno(filepath)
        elif command == "mp":
            audioplayer(filepath)
        elif command == "mkdir":
            display_help()
        elif command == "PythonOS1":
            start_python_operating_system()
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' for a list of commands.")
