
import tkinter as tk
import os 
import sys
import subprocess
import file
import configparser
from tkinter import messagebox
from file import config_file, panno , pyle, addons, home_dir
from openrun import run_with_python_ide

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


def desktop_start_construct():
    import configparser
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

# Read configuration file
config = configparser.ConfigParser()
config.read(config_path)

# Create main window
root = tk.Tk()
root.title(config['GUI']['title'])
root.geometry(config['GUI']['geometry'])

# Create taskbar
taskbar_height = int(config['GUI']['taskbar_height'])
taskbar_color = config['GUI']['taskbar_color']
taskbar_name = config['GUI']['taskbar_name']
taskbar = tk.Frame(root, height=taskbar_height, bg=taskbar_color)
taskbar.pack(side=tk.TOP, fill=tk.X)

# Create desktop
desktop = tk.Frame(root, bg=config['GUI']['background_color'])
desktop.pack(expand=True, fill=tk.BOTH)
desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))

# Create file context menu
file_context_menu = tk.Menu(root, tearoff=False)

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
        label.bind("<Button-3>", lambda event, path=file_path: show_file_context_menu(event, path))
        label.grid(row=grid_row, column=grid_column, padx=10, pady=10, sticky='w')

        grid_column += 1
        if grid_column == grid_columns:
            grid_column = 0
            grid_row += 1

def delete_file(home_dir):
    if os.path.isfile(home_dir):
        os.remove(home_dir)
        print(f'{home_dir} has been deleted.')


delete_file('home_dir')
load_files()

def show_file_context_menu(event, home_dir):
    context_menu = tk.Menu(desktop, tearoff=0)

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
    
    context_menu.add_command(label='Delete', command=lambda: (delete_file(home_dir), load_files()))

    context_menu.post(event.x_root, event.y_root)
    load_files()


def create_file(home_directory):
    # create home directory if it doesn't exist
    if not os.path.exists(home_directory):
        os.mkdir(home_directory)

    # create filename
    filename = 'file{}.py'.format(len(os.listdir(home_directory)))

    # create file path
    file_path = os.path.join(home_directory, filename)

    # write to file
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            file.write('This is the content of {}\n'.format(filename))
            print("File created: {}".format(filename))
    else:
        print("File already exists: {}".format(filename))

    # reload files
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

        