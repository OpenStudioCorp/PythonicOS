import os
import tkinter as tk
from tkinter import ttk, messagebox

def open_file():
    selected_item = tree.focus()
    if selected_item:
        file_path = tree.item(selected_item)['text']
        extension = os.path.splitext(file_path)[1]
        if extension in ['.txt', '.doc', '.pdf']:
            # Open the file using the appropriate command
            messagebox.showinfo('Open File', f'Opening file: {file_path}')
            # Replace the line below with the appropriate command based on the file extension
            # For example, you can use 'os.startfile(file_path)' to open the file with the default program

def search_files():
    query = search_var.get()
    tree.delete(*tree.get_children())  # Clear the tree view

    for sta, dirs, files in os.walk(directory):
        for file in files:
            if query.lower() in file.lower():
                tree.insert('', 'end', text=os.path.join(sta, file), open=True)

# Create the Tkinter sta instance
root = tk.Tk()
root.title('File Browser')

# Specify the directory to search
directory = os.getcwd()  # Replace with the desired directory path

# Create the tree view
tree = ttk.Treeview(root)
tree.pack(fill='both', expand=True)

# Create the right-click menu
menu = tk.Menu(root, tearoff=False)
menu.add_command(label='Open', command=open_file)

def popup(event):
    selected_item = tree.focus()
    if selected_item:
        menu.post(event.x_root, event.y_root)

tree.bind('<Button-3>', popup)



# Create the search bar
search_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_var)
search_entry.pack(fill='x')
search_entry.bind('<KeyRelease>', lambda event: search_files())

# Initially display the files in the specified directory
for sta, dirs, files in os.walk(directory):

    for file in files:
        tree.insert('', 'end', text=os.path.join(sta, file), open=True)

root.mainloop()
