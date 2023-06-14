import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Set the directory to scan for .py files
directory = os.getcwd()

# Create the main window
root = tk.Tk()
root.title("App Launcher")
root.geometry("500x500")
root.configure(bg="white")
# Create a list to hold the file names
file_list = []

# Scan the directory for .py files and add them to the list
for file in os.listdir(directory):
    if file.endswith(".py"):
        # Split the filename and extension
        file_name, file_ext = os.path.splitext(file)
        # Add the filename to the list
        file_list.append(file_name)

# Create a listbox to display the file names
listbox = tk.Listbox(root)
listbox.pack()
listbox.config(width=50, height=20)

# Add the file names to the listbox
for file_name in file_list:
    listbox.insert(tk.END, file_name)

# Create a function to open the selected file
def open_file():
    # Get the selected file name
    selection = listbox.curselection()
    if selection:
        file_name = file_list[selection[0]]
        # Open the file in a new window
        os.system(f"python {file_name}.py")

# Create a button to open the selected file
open_button = ttk.Button(root, text="Open", command=open_file)
open_button.pack()

# Start the main loop
root.mainloop()