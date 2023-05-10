import subprocess
from tkinter import messagebox
import tkinter as tk
from file import pyle,panno,home_dir
import os
import configparser
root = tk.Tk()
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)
desktop = tk.Frame(root, bg=config['GUI']['background_color'])


def run_with_python_ide(home_di):
    try:
        subprocess.Popen(['idle', '-r', 'home_dir'])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system!.')


def run_with_pyle(home_di):
    try:
        subprocess.Popen(['python', pyle], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(home_file):
    try:
        subprocess.Popen(['python', panno], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')

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

        # label.bind("<Button-1>", lambda event, path=file_path: open_file(path))
        
        label.grid(row=grid_row, column=grid_column, padx=10, pady=10, sticky='w')

        grid_column += 1
        if grid_column == grid_columns:
            grid_column = 0
            grid_row += 1