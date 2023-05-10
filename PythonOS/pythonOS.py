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
from fileactions import  desktop_start_construct,create_file,start_rename,file_context_menu,show_file_context_menu,desktop_right_click,finish_rename,taskbar,taskbar_color,taskbar_height,taskbar_name,pin_to_taskbar,unpin_from_taskbar, load_files,find_label,delete_file,desktop,home_dir
import openrun
from openrun import run_with_panno, run_with_pyle, run_with_python_ide,open_file

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





root = tk.Tk()
root.title("PythonOS")
root.geometry("640x480")
root.mainloop()
taskbar = tk.Frame(root, height=40, bg='lightgrey')
taskbar.pack(side=tk.TOP, fill=tk.X)

desktop = tk.Frame(root, bg='grey')
desktop.pack(expand=True, fill=tk.BOTH)
desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
file_context_menu = tk.Menu(root, tearoff=False)
script_dir = os.path.dirname(os.path.abspath(__file__))


def loggedin():
    

    def main():
        desktop_start_construct()
    load_files()









if __name__ == "__main__":
    start()