import tkinter as tk
from tkinter import ttk
import os
import sys
import sysconfig
import desktop
import loginscreen as lsc
import argparse
from desktop import load_files,taskbar,taskbar_color,run_with_panno,run_with_pyle,run_with_python_ide,start_rename,finish_rename,refresh_code,desktop_right_click,root,taskbar_height,taskbar_name,pin_to_taskbar,unpin_from_taskbar,create_file,configparser,show_file_context_menu,file_context_menu,file_path,filepath,find_label,open_file,delete_file,open_html_file,home_directory,keyboard,config,script_path,script_path1,script_dir,is_pinned,panno,show_popup,script_path0,app,argparse,QWebEngineView,math,messagebox,desktop,subprocess,sys
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-start', help='start the main program!')
args = parser.parse_args()

def start():
    import configparser
config = configparser.ConfigParser()
config.read('config.ini')

def login():
    
    username = username_entry.get()
    password = password_entry.get()
    
    # Read passwords from configuration file
    config_file = os.path.join(os.path.dirname(__file__), 'pass.ini')
    config = configparser.ConfigParser()
    config.read(config_file)
    print(config.sections())  # Debugging line
    print(config.options('login'))  # Debugging line
    # Check if entered username and password match the ones in the configuration file
    if username in config['login'] and config['login'][username] == password:
        print("Login successful!")
        root.destroy()  # Close the login window

    else:
        print("Incorrect username or password.")
    password_entry.delete(0, tk.END)

# Create main window
if args.part == 'A':
    root = tk.Tk()
root.title('Login')

# Create login form
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

# Run the main event loop
root.mainloop()

def loggedin():
    login()

def main():
    desktop_start_construct()
    load_files()

if args.part == 'start':
    print('Running start of the code')
    # Code for part A goes here
    login()
else:
    print('Invalid argument')

def desktop_start_construct():
    #createe main window when logged in
    root = tk.Tk()
    root.title(config['GUI']['title'])
    root.geometry(config['GUI']['geometry'])

    # Create taskbar
    taskbar_height = int(config['GUI']['taskbar_height'])
    taskbar_color = config['GUI']['taskbar_color']
    taskbar_name = config['GUI']['taskbar_name']
    taskbar = tk.Frame(root, height=taskbar_height, bg=taskbar_color)
    taskbar.pack(side=tk.TOP, fill=tk.X)
    # Create desktop
    desktop = tk.Frame(root, bg=config['GUI']['background_color'])
    desktop.pack(expand=True, fill=tk.BOTH)
    desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
    # Create file context menu
    file_context_menu = tk.Menu(root, tearoff=False)
    # Load files onto the desktop
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_files()
    root.mainloop()
    root = tk.Tk()
    root.title("PthonOS")
    root.geometry("640x480")
    taskbar = tk.Frame(root, height=40, bg='lightgrey')
    taskbar.pack(side=tk.TOP, fill=tk.X)
    desktop = tk.Frame(root, bg='grey')
    desktop.pack(expand=True, fill=tk.BOTH)
    desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
    file_context_menu = tk.Menu(root, tearoff=False)
    script_dir = os.path.dirname(os.path.abspath(__file__))


    if __name__ == "__main__":
     login()