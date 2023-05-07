import os
import tkinter as tk
def create_file():
    filename = 'file{}.txt'.format(len(os.listdir(current_folder_path)))
    filepath = os.path.join(current_folder_path, filename)
    with open(filepath, 'w') as file:
        file.write('This is the content of {}'.format(filename))
    load_files(current_folder_path, file_listbox)

def load_files(folder_path, listbox):
    listbox.delete(0, tk.END)
    files = sorted(os.listdir(folder_path))
    for file in files:
        listbox.insert(tk.END, file)
