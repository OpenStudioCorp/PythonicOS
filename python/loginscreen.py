# loginscreen.py
import subprocess
import tkinter as tk
import configparser
import os
import argparse
import configparser
import file
from file import usrpass,config_login,shell
root = tk.Tk()

config = configparser.ConfigParser()
config.read(config_login)

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Read passwords from configuration file
    config_file = os.path.join(os.path.dirname(__file__), 'pass.ini')
    config = configparser.ConfigParser()
    config.read(config_file)

    # Check if entered username and password match the ones in the configuration file
    if username in config['login'] and config['login'][username] == password:
        print("Login successful!")
        
        subprocess.Popen(["python3", 'PythonOS/shell.py'])
        print('cat')
        root.destroy()  # Close the login window
    else:
        print("Incorrect username or password.")


# Create login form
root.geometry('140x140')
username_label = tk.Label(root, text='Username')
username_entry = tk.Entry(root)
password_label = tk.Label(root, text='Password')
password_entry = tk.Entry(root, show='*')
login_button = tk.Button(root, text='Login', command=login)
# Add widgets to the window
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

# Create root window


# Call login() after the root window has been created
login()

# Start the event loop
root.mainloop()