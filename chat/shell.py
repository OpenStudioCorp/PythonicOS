import os
import subprocess
import sys
from loginscreen import login
var = sys.stdin.read()
def open():
    print()

def play():
    print()
    
    def PythonicOS():
        print('welcome to PythonicOS')

        def loggedin(var):
        
            if var == 'True':
                
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
                        help()
                    elif command == "open":
                        open()
                    elif command == "play":
                        play()

                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "help":
                        help()
                    elif command == "exit":
                        print("Goodbye!")
                        break
                    else:
                        print("Unknown command. Type 'help' for a list of commands.")







def help():
    print("-------------")
    print("cd <directory>: Changes the current working directory to the specified directory.")
    print("help: Displays this help message.")
    print("exit: Exits MyShell.\n")
    print('mkdir: makes a directory')
    print("panno; creates a file")
    print("mp: opens a music player")
if __name__ == "__main__":
    loggedin(var)