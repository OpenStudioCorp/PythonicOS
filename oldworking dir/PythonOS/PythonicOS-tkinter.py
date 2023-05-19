import tkinter as tk
import subprocess
import json
import keyboard
from tkinter import messagebox
import sys, os
import time
import argparse
import math

import configparser
def start_rename(home_dir):
    label = find_label(home_dir)
    entry = tk.Entry(label, relief=tk.FLAT)
    entry.insert(0, os.path.basename(home_dir))
    entry.bind("<Return>", lambda event, path=home_dir, entry=entry: finish_rename(path, entry))
    entry.bind("<FocusOut>", lambda event, entry=entry: entry.destroy())
    entry.pack()
    entry.select_range(0, tk.END)
    entry.focus()


def finish_rename(home_dir, entry):
    new_filename = entry.get().strip()
    new_home_dir = os.path.join(os.path.dirname(home_dir), new_filename)
    os.rename(home_dir, new_home_dir)
    if is_pinned(home_dir):
        unpin_from_taskbar(home_dir)
        pin_to_taskbar(new_home_dir)
    load_files()


def pin_to_taskbar(home_dir):
    if not is_pinned(home_dir):
        taskbar_label = tk.Label(taskbar, text=os.path.basename(home_dir), padx=10)
        taskbar_label.pack(side=tk.LEFT)

        def open_pinned_file():
            subprocess.call(['nano', home_dir])

        taskbar_label.bind("<Button-1>", lambda event, path=home_dir: open_pinned_file())


def unpin_from_taskbar(home_dir):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            widget.destroy()


def find_label(home_dir):
    for widget in desktop.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            return widget


def is_pinned(home_dir):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            return True
        return False

config = 'config.ini'
home_dir = os.getcwd()
# !/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "charlie!"
__version__ = "0.1.0"
__license__ = "construct1.0"


def create_file(home_dir):
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)

    filename = 'file{}.py'.format(len(os.listdir(home_dir)))

    with open(home_dir, 'w') as file:
        file.write('This is the content of {}'.format(filename))
        print("print com1")
    load_files()
    
def show_popup(message):
    popup = tk.Tk()
    popup.wm_title("Popup")
    label = tk.Label(popup, text=message)
    label.pack()
    popup.after(3000, lambda: popup.destroy())  # Close the popup after 3000 milliseconds (3 seconds)
    popup.mainloop()


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
        home_dir = os.path.join(files_path, file)
        label = tk.Label(desktop, text=file, pady=10)

        # Get the file extension
        _, extension = os.path.splitext(home_dir)

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

        label.bind("<Button-1>", lambda event, path=home_dir: open_file(path))
        label.bind("<Button-3>", lambda event, path=home_dir: show_files_context_menu(event))
        label.grid(row=grid_row, column=grid_column, padx=10, pady=10, sticky='w')

        grid_column += 1
        if grid_column == grid_columns:
            grid_column = 0
            grid_row += 1

# import configparser and the config.ini file
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

# Read configuration file
config = configparser.ConfigParser()
config.read(config_path)

# Create main window
root = tk.Tk()
root.title('cat')
root.geometry('640x480')

# Create taskbar
taskbar_height = '50'
taskbar_color = 'blue'
taskbar_name = 'taskbar'
taskbar = tk.Frame(root, height=taskbar_height, bg=taskbar_color)
taskbar.pack(side=tk.TOP, fill=tk.X)

# Create desktop
desktop = tk.Frame(root, bg='lightblue')
desktop.pack(expand=True, fill=tk.BOTH)

# Create file context menu
file_context_menu = tk.Menu(root, tearoff=False)

def show_files_context_menu(event):
    context_menu = tk.Menu(desktop, tearoff=0)
    home_dir = os.getcwd()
    # Add "Open" option to the right-click menu
    context_menu.add_command(label='Open', command=lambda: open_file(home_dir))
    if not is_pinned(home_dir):
        context_menu.add_command(label='pin to task bar', command=lambda: pin_to_taskbar(home_dir))
    if is_pinned(home_dir):
        context_menu.add_command(label='unpin from task bar', command=lambda: unpin_from_taskbar(home_dir))

    if home_dir.endswith('.py'):
        context_menu.add_command(label='Run with Python IDE', command=lambda: run_with_python_ide(home_dir))
        context_menu.add_command(label='Run with panno', command=lambda: run_with_panno(home_dir))

    if home_dir.endswith('.html'):
        context_menu.add_command(label='Open with Browser', command=lambda: run_with_pyle(home_dir))

        if home_dir.endswith('.txt'):
            context_menu.add_command(label='Open with panno', command=lambda: run_with_panno(home_dir))

        if home_dir.endswith('.cs'):
            context_menu.add_command(label='Open with panno', command=lambda: run_with_panno(home_dir))

    context_menu.add_command(label='Rename', command=lambda: start_rename(home_dir))
    context_menu.add_command(label='panno!', command=lambda: run_with_panno(home_dir))
    context_menu.add_command(label='Refresh', command=lambda: refresh_code())
    context_menu.add_command(label='Delete', command=lambda: (delete_file(home_dir), load_files()))

    load_files()
    context_menu.post(event.x_desktop, event.y_desktop)

    
# Bind the function to the right-click event on the desktop
desktop.bind("<Button-3>", show_files_context_menu)

# Run the Tkinter event loop
root.mainloop()

script_dir = os.path.dirname(os.path.abspath(__file__))
load_files()
# load basic info about the monitor and menus
# ------------------------------------------#
# load the scripts that are used in the file such as pyle and panno!
script_path0 = os.path.join(script_dir, 'addons', 'panno.py')
script_path1 = os.path.join(script_dir, 'addons', 'pyle.py')


# ------------------------------------------#
def delete_file(home_dir):
    if os.path.isfile(home_dir):
        os.remove(home_dir)
        print(f'{home_dir} has been deleted.')


delete_file('home_dir')
load_files()



# ---------------------------------------------#
# open file allows you to open files with diffrent editors, panno is the most used for writing python,css,js ect, and pyle is a webbrowser that allows you to navagate the web!
# ---------------------------------------------#
def open_file(home_dir):
    try:
        if home_dir.endswith('.cs'):
            subprocess.Popen(['notepad', home_dir])
        elif home_dir.endswith('.html'):
            run_with_panno([home_dir])
        elif home_dir.endswith('.txt'):
            run_with_panno([home_dir])
        else:
            subprocess.Popen(['notepad', home_dir])
    except FileNotFoundError:
        messagebox.showerror('Open File', 'Default program not found for the file extension.')






def refresh_code():
    load_files()
# ---------------------------------------------#
# show file context menu, basicly the right click menu within windows and mac. this one is the ols menu or the actual usefull menu, this one is activated when you press show old menu or you call show_desktop_context_menu
# ---------------------------------------------#


# Bind the function to the right-click event
desktop.bind("<Button-3>", show_files_context_menu)


# ---------------------------------------------#

# ---------------------------------------------#

def run_with_python_ide(home_dir):
    try:
        subprocess.Popen(['idle', '-r', 'home_dir'])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is somehow broken,.')


def run_with_pyle(home_dir):
    try:
        subprocess.Popen(['python', script_path1], cwd=script_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(home_dir):
    try:
        subprocess.Popen(['python', script_path0], cwd=script_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')


# --------------------------------------------#

# def run_with_python_ide(home_dir):
#     try:
#         subprocess.Popen(['idle', '-r', home_dir])
#     except FileNotFoundError:
#         messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system.')

# def run_with_python_ide(home_dir):
#     try:
#         subprocess.Popen(['idle', '-r', home_dir])
#     except FileNotFoundError:
#         messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system.')


# def desktop_right_click(event,path,home_dir):
#     # Create the context menu
    
#     context_menu = tk.Menu(desktop, tearoff=0)

#     # Add "file creation" option to the context menu
#     context_menu.add_command(label="html", command=lambda: create_file(path))  # Provide the appropriate file path

#     # Add a separator line
#     context_menu.add_separator()

#     # Add "Run with Python IDE" option to the context menu
#     context_menu.add_command(label="open old menu", command=lambda: show_file_context_menu(event, path))  # Provide the appropriate file path

#     # Display the context menu at the clicked coordinates
#     context_menu.post(event.x_root, event.y_root)


# Bind the right-click event to the desktop window

script_path = os.path.dirname(os.path.abspath(__file__))
home_directory = os.path.join(script_path, 'home')





# -------------------------------------------------#
# this part is used for hotkeys!

# -------------------------------------------------#


load_files()

root.mainloop()