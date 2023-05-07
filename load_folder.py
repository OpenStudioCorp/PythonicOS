import tkinter as tk
from tkinter import ttk 
import os

root = tk.Tk()
root.title("PythonOS file explorer")
root.geometry("640x480")

taskbar = tk.Frame(root, height=40,bg='lightgrey')
taskbar.pack(side=tk.TOP, fill=tk.X)

desktop = tk.Frame(root, bg='grey')
desktop.pack(expand=True, fill=tk.BOTH)
desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
file_context_menu = tk.Menu(root, tearoff=False)
script_dir = os.path.dirname(os.path.abspath(__file__))


def load_files(files_, directory_path):
    for widget in desktop.winfo_children():
        widget.destroy()

    # Create a frame to hold the file explorer widget
    file_explorer_frame = tk.Frame(desktop, bd=2, relief='sunken')
    file_explorer_frame.pack(side='left', fill='y')

    # Create a treeview widget to display the directory structure
    tree = ttk.Treeview(file_explorer_frame)
    tree.pack(side='left', fill='y')
    tree.bind("<Double-1>", lambda event: open_file(tree))

    # Create a scrollbar for the treeview widget
    scrollbar = ttk.Scrollbar(file_explorer_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side='right', fill='y')
    tree.configure(yscrollcommand=scrollbar.set)

    # Add the root node to the treeview
    root_node = tree.insert('', 'end', text=directory_path, open=True)

    # Add child nodes to the root node for each file and directory in the specified directory
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isdir(file_path):
            dir_node = tree.insert(root_node, 'end', text=file, open=False)
            add_nodes_to_tree(tree, dir_node, file_path)
        else:
            tree.insert(root_node, 'end', text=file)

def add_nodes_to_tree(tree, parent_node, directory_path):
    # Recursively add child nodes to the parent node for each file and directory in the specified directory
    for file in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file)
        if os.path.isdir(file_path):
            dir_node = tree.insert(parent_node, 'end', text=file, open=False)
            add_nodes_to_tree(tree, dir_node, file_path)
        else:
            tree.insert(parent_node, 'end', text=file)
            load_files()