from pythonOS import desktop
import tkinter as tk
import os 
import sys
import subprocess
import file
from tkinter import messagebox
from file import config_file, panno , pyle, addons
from pythonOS import load_files,home_directory, taskbar, show_file_context_menu

def create_file(home_directory):
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)

    filename = 'file{}.py'.format(len(os.listdir(home_directory)))

    with open(home_directory, 'w') as file:
        file.write('This is the content of {}'.format(filename))
        print("print com1")
    load_files()

def desktop_right_click(event):
    # Create the context menu
    context_menu = tk.Menu(desktop, tearoff=0)

    # Add "file creation" option to the context menu
    context_menu.add_command(label="html", command=lambda: create_file(home_directory))  # Provide the appropriate file path

    # Add a separator line
    context_menu.add_separator()

    # Add "Run with Python IDE" option to the context menu
    context_menu.add_command(label="open old menu", command=lambda: show_file_context_menu(event,home_directory))  # Provide the appropriate file path

    # Display the context menu at the clicked coordinates
    context_menu.post(event.x_root, event.y_root)


# Bind the right-click event to the desktop window
desktop.bind("<Button-3>", desktop_right_click)

script_path = os.path.dirname(os.path.abspath(__file__))
home_directory = os.path.join(script_path, 'documenta')


def start_rename(home_directory):
    label = find_label(home_directory)
    entry = tk.Entry(label, relief=tk.FLAT)
    entry.insert(0, os.path.basename(home_directory))
    entry.bind("<Return>", lambda event, path=home_directory, entry=entry: finish_rename(path, entry))
    entry.bind("<FocusOut>", lambda event, entry=entry: entry.destroy())
    entry.pack()
    entry.select_range(0, tk.END)
    entry.focus()


def finish_rename(home_directory, entry):
    new_filename = entry.get().strip()
    new_home_directory = os.path.join(os.path.dirname(home_directory), new_filename)
    os.rename(home_directory, new_home_directory)
    if is_pinned(home_directory):
        unpin_from_taskbar(home_directory)
        pin_to_taskbar(new_home_directory)
    load_files()


def pin_to_taskbar(home_directory):
    if not is_pinned(home_directory):
        taskbar_label = tk.Label(taskbar, text=os.path.basename(home_directory), padx=10)
        taskbar_label.pack(side=tk.LEFT)

        def open_pinned_file():
            subprocess.call(['nano', home_directory])

        taskbar_label.bind("<Button-1>", lambda event, path=home_directory: open_pinned_file())
        taskbar_label.bind("<Button-3>", lambda event, path=home_directory: show_file_context_menu(event, path))


def unpin_from_taskbar(home_directory):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_directory):
            widget.destroy()


def find_label(home_directory):
    for widget in desktop.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_directory):
            return widget


def is_pinned(home_directory):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_directory):
            return True
        return False
    
    def run_with_python_ide(home_directory):
        try:
            subprocess.Popen(['idle', '-r', 'home_directory'])
        except FileNotFoundError:
            messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system!.')


def run_with_pyle(home_directory):
    try:
        subprocess.Popen(['python', pyle], cwd=addons)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(home_directory):
    try:
        subprocess.Popen(['python', panno], cwd=addons)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')