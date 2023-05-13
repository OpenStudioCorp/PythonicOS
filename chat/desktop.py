import tkinter as tk
import subprocess
import json
import addons.panno as panno
import keyboard
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from tkinter import messagebox
import sys, os
import time
import argparse
import math
import configparser

config = 'config.ini'

# !/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "charlie!"
__version__ = "0.1.0"
__license__ = "construct1.0"

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "home")
file_path = os.path.join(script_dir, "home")


def create_file(filepath):
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)

    filename = 'file{}.py'.format(len(os.listdir(filepath)))

    with open(file_path, 'w') as file:
        file.write('This is the content of {}'.format(filename))
        print("print com1")
    load_files()


# -----------------------------------------#
# welcome to desktopy! this script land is kinda junk atm as i am still working on adding features to it literaly every seccond and fixxing erros aswell
# this part will explain the functions you can call when you want to make a addon,
#
# basic things first
# filepath is the home dir!
# restart_script will refresh the desktop when run!
# load_files() refreshes the desktop,
# run_with_panno(filepath) runs the file that was right clicked with panno
# run_with_pyle runs the web browsers
# currently the desktop doesnt allow you to create files!
#
#
#
#
#
#
#
#
#
#
#
#
#
# -----------------------------------------#
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

# import configparser and the config.ini file
import configparser
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
# load basic info about the monitor and menus
# ------------------------------------------#
# load the scripts that are used in the file such as pyle and panno!
script_path0 = os.path.join(script_dir, 'addons', 'panno.py')
script_path1 = os.path.join(script_dir, 'addons', 'pyle.py')


# ------------------------------------------#
def delete_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
        print(f'{filepath} has been deleted.')


delete_file('filepath')
load_files()
app = QApplication(sys.argv)


# ---------------------------------------------#
# open file allows you to open files with diffrent editors, panno is the most used for writing python,css,js ect, and pyle is a webbrowser that allows you to navagate the web!
# ---------------------------------------------#
def open_file(filepath):
    try:
        if filepath.endswith('.cs'):
            subprocess.Popen(['notepad', filepath])
        elif filepath.endswith('.html'):
            run_with_panno([filepath])
        elif filepath.endswith('.txt'):
            run_with_panno([filepath])
        else:
            subprocess.Popen(['notepad', filepath])
    except FileNotFoundError:
        messagebox.showerror('Open File', 'Default program not found for the file extension.')


app = QApplication(sys.argv)


def open_html_file(filepath):
    app = QApplication(sys.argv)

    # Create a QWebEngineView instance
    web_view = QWebEngineView()

    # Load the local file
    web_view.load(QUrl.fromLocalFile(filepath))

    # Show the browser window
    web_view.show()

    # Run the application event loop
    sys.exit(app.exec_())

def refresh_code():
    load_files()
# ---------------------------------------------#
# show file context menu, basicly the right click kmenu within windows, and mac. this one is the ols menu or the actual usefull menu, this one is activated when you press show old menu or you call show_desktop_context_menu
# ---------------------------------------------#
def show_file_context_menu(event, filepath):
    context_menu = tk.Menu(desktop, tearoff=0)

    # Add "Open" option to the right-click menu
    context_menu.add_command(label='Open', command=lambda: open_file(filepath))
    if not is_pinned(filepath):
        context_menu.add_command(label='pin to task bar', command=lambda: pin_to_taskbar(filepath))
    if is_pinned(filepath):
        context_menu.add_command(label='unpin from task bar', command=lambda: unpin_from_taskbar(filepath))

    if filepath.endswith('.py'):
        context_menu.add_command(label='Run with Python IDE', command=lambda: run_with_python_ide(filepath))
        context_menu.add_command(label='Run with panno', command=lambda: run_with_panno(filepath))

    if filepath.endswith('.html'):
        context_menu.add_command(label='Open with Browser', command=lambda: run_with_pyle(filepath))

        if filepath.endswith('.txt'):
            context_menu.add_command(label='Open with panno', command=lambda: run_with_panno(filepath))

        if filepath.endswith('.cs'):
            context_menu.add_command(label='Open with panno', command=lambda: run_with_panno(filepath))

    context_menu.add_command(label='Rename', command=lambda: start_rename(filepath))
    context_menu.add_command(label='panno!', command=lambda: run_with_panno(filepath))
    context_menu.add_command(label='Refresh', command=lambda: refresh_code())
    context_menu.add_command(label='Delete', command=lambda: (delete_file(filepath), load_files()))

    context_menu.post(event.x_root, event.y_root)
    load_files()


# ---------------------------------------------#

# ---------------------------------------------#

def run_with_python_ide(filepath):
    try:
        subprocess.Popen(['idle', '-r', 'filepath'])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system!.')


def run_with_pyle(filepath):
    try:
        subprocess.Popen(['python', script_path1], cwd=script_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(filepath):
    try:
        subprocess.Popen(['python', script_path0], cwd=script_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')


# --------------------------------------------#

# def run_with_python_ide(filepath):
#     try:
#         subprocess.Popen(['idle', '-r', filepath])
#     except FileNotFoundError:
#         messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system.')

# def run_with_python_ide(filepath):
#     try:
#         subprocess.Popen(['idle', '-r', filepath])
#     except FileNotFoundError:
#         messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system.')


def desktop_right_click(event):
    # Create the context menu
    context_menu = tk.Menu(desktop, tearoff=0)

    # Add "file creation" option to the context menu
    context_menu.add_command(label="html", command=lambda: create_file(filepath))  # Provide the appropriate file path

    # Add a separator line
    context_menu.add_separator()

    # Add "Run with Python IDE" option to the context menu
    context_menu.add_command(label="open old menu", command=lambda: show_file_context_menu(event,filepath))  # Provide the appropriate file path

    # Display the context menu at the clicked coordinates
    context_menu.post(event.x_root, event.y_root)


# Bind the right-click event to the desktop window
desktop.bind("<Button-3>", desktop_right_click)

script_path = os.path.dirname(os.path.abspath(__file__))
home_directory = os.path.join(script_path, 'documenta')


def start_rename(filepath):
    label = find_label(filepath)
    entry = tk.Entry(label, relief=tk.FLAT)
    entry.insert(0, os.path.basename(filepath))
    entry.bind("<Return>", lambda event, path=filepath, entry=entry: finish_rename(path, entry))
    entry.bind("<FocusOut>", lambda event, entry=entry: entry.destroy())
    entry.pack()
    entry.select_range(0, tk.END)
    entry.focus()


def finish_rename(filepath, entry):
    new_filename = entry.get().strip()
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    os.rename(filepath, new_filepath)
    if is_pinned(filepath):
        unpin_from_taskbar(filepath)
        pin_to_taskbar(new_filepath)
    load_files()


def pin_to_taskbar(filepath):
    if not is_pinned(filepath):
        taskbar_label = tk.Label(taskbar, text=os.path.basename(filepath), padx=10)
        taskbar_label.pack(side=tk.LEFT)

        def open_pinned_file():
            subprocess.call(['nano', filepath])

        taskbar_label.bind("<Button-1>", lambda event, path=filepath: open_pinned_file())
        taskbar_label.bind("<Button-3>", lambda event, path=filepath: show_file_context_menu(event, path))


def unpin_from_taskbar(filepath):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            widget.destroy()


def find_label(filepath):
    for widget in desktop.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            return widget


def is_pinned(filepath):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            return True
        return False


# -------------------------------------------------#
# this part is used for hotkeys!

# -------------------------------------------------#


load_files()

root.mainloop()