import tkinter as tk
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

from create_file import create_file, load_files
from open_file import open_file, open_html_file
from context_menu import show_file_context_menu
from pin_taskbar import pin_to_taskbar, unpin_from_taskbar

# Set the initial folder path
current_folder_path = ""  # Change this to the desired folder path

# Create the main window
root = tk.Tk()
root.title("File Manager")
root.geometry("640x480")

# Create the file listbox
file_listbox = tk.Listbox(root, width=50)
file_listbox.pack(fill=tk.BOTH, expand=True)

# Create the create file button
create_button = tk.Button(root, text="Create File", command=create_file)
create_button.pack(pady=10)

# Load the files initially
load_files(current_folder_path, file_listbox)

def create_folder():
    foldername = 'folder{}'.format(len(os.listdir('files')))
    folderpath = os.path.join('files', foldername)
    os.makedirs(folderpath)
    load_files(current_folder_path)

def open_folder(folder_path):
    global current_folder_path
    current_folder_path = os.path.join(current_folder_path, folder_path)
    load_files(current_folder_path)

    back_button = tk.Button(desktop, text="Back", command=go_back)
    back_button.grid(row=0, column=0, padx=10, pady=10, sticky='w')

def go_back():
    global current_folder_path
    current_folder_path = os.path.dirname(current_folder_path)
    load_files(current_folder_path)

# Create Folder button
create_folder_button = tk.Button(taskbar, text="Create Folder", command=create_folder)
create_folder_button.pack(side=tk.LEFT, padx=10)

# Load initial files
load_files(current_folder_path)

root.mainloop()

