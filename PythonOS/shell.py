import os

def print_greetings():
    print("Welcome to MyShell!")
    print("Version 1.0")

def print_help():
    print("Here are the available commands:")
    print("cd <directory>: Change current working directory to <directory>")
    print("help: Display this help message")
    print("exit: Exit MyShell")

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
        elif tokens[0] == "exit":
            break
        else:
            print(f"{tokens[0]}: command not found")

if __name__ == "__main__":
    my_shell()
