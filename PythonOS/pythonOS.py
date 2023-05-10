import tkinter as tk
from tkinter import ttk
import os
import sys
import sysconfig
import configparser
import argparse
import file
import fileactions
import openrun
from openrun import run_with_panno, run_with_pyle, open_file,run_with_python_ide
import subprocess
from file import config_file, home_dir
from fileactions import  create_file,start_rename,show_file_context_menu,desktop_right_click,finish_rename,taskbar,taskbar_color,taskbar_height,taskbar_name,pin_to_taskbar,unpin_from_taskbar, load_files,find_label,delete_file,desktop,home_dir
import openrun
from openrun import run_with_panno, run_with_pyle, run_with_python_ide,open_file

def load_files():
    for widget in desktop.winfo_children():
        widget.destroy()

    files_path = 'files'
    if not os.path.exists(files_path):
        os.makedirs(files_path)
    files = sorted(os.listdir(files_path))  # Sort files alphabetically
    grid_columns = 5
    grid_row = 0
    grid_column = 0

    for file in files:
        file_path = os.path.join(files_path, file)
        label = tk.Label(desktop, text=file, pady=10)

        # Get the file extension
        _, extension = os.path.splitext(file_path)

        # Set the background color based on the file extension
        if extension == '.cs':
            label.configure(background='lightblue')
        elif extension == '.html':
            label.configure(background='red')
        elif extension == '.py':
            label.configure(background='yellow')
        elif extension == '.css':
            label.configure(background='blue')
        elif extension == '.js':
            label.configure(background='orange')
        elif extension == '.txt':
            label.configure(background='white')

        label.bind("<Button-1>", lambda event, path=file_path: open_file(path))
        label.bind("<Button-3>", lambda event, path=file_path: show_file_context_menu(event, path))
        label.grid(row=grid_row, column=grid_column, padx=10, pady=10, sticky='w')

        grid_column += 1
        if grid_column == grid_columns:
            grid_column = 0
            grid_row += 1

import configparser
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

# Read configuration file
config = configparser.ConfigParser()
config.read(config_path)

# Create main window
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

load_files()


def start():
    
    load_files()
    import configparser
config = configparser.ConfigParser()
config.read('config.ini')


            


# Load files onto the desktop
script_dir = os.path.dirname(os.path.abspath(__file__))
load_files()

def desktop_right_click(event):
    # Create the context menu
    context_menu = tk.Menu(desktop, tearoff=0)

    # Add "file creation" option to the context menu
    context_menu.add_command(label="new file", command=lambda: create_file(home_dir))  # Provide the appropriate file path

    # Add a separator line
    context_menu.add_separator()

    # Add "Run with Python IDE" option to the context menu
    context_menu.add_command(label="open old menu", command=lambda: show_file_context_menu(event,home_dir))  # Provide the appropriate file path

    # Display the context menu at the clicked coordinates
    context_menu.post(event.x_root, event.y_root)


# Bind the right-click event to the desktop window
desktop.bind("<Button-3>", desktop_right_click)

def delete_file(home_dir):
    if os.path.isfile(home_dir):
        os.remove(home_dir)
        print(f'{home_dir} has been deleted.')


delete_file('home_dir')
load_files()

















if __name__ == "__main__":
    start()