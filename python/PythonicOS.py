# import the things that we need, even the ones that we don't need
from json import load
import tkinter as tk
import tkinter.font as tkFont
import subprocess
from tkinter import messagebox
import sys
import time
import configparser
import os
import shutil
import datetime
import file
from file import pycrashos, pycrashnone, pycrashshell,pycrashconfig, shell, config_file, usrpass, config_login
import logging
import argparse
from tkinter import ttk  # Normal Tk widgets don't look good on Mac and Linux, and also some of the code in this file uses ttk, idk why?
root = tk.Tk()
# subprocess.call('setup.py')
#-----------------------------------#
#   welcome to PythonicOS's desktop module
#   this module should not be touched unless you know what your doing and you have a backup of it!
#   this module is the main module of the OS, it is the desktop, it is the thing that you see when you open the OS
#   it has multiple functions that allow you to do things like open files, create files, delete files, and more!
#-----------------------------------#
#  functions in this module: 
#   start_rename(home_dir, label)
#   finish_rename(home_dir, entry)
#   delete_file(home_dir)
#   pin_to_taskbar(home_dir)
#   unpin_from_taskbar(home_dir)
#   is_pinned(home_dir)
#   open_file(home_dir)
#   load_files_thread(home_dir)
#   create_file(home_dir)
#   create_folder(home_dir)
#   delete_folder(home_dir)
#-----------------------------------#
#   variables in this module:
#   syst
#   system
#   home_dir
#   sys_bin
#   sys_scripts
#   sys_addr
#   sys_docu
#   sys_hom_usr
#   sys_hom_usr_doc
#   sys_hom_usr_doc_pro
#   sys_logs
#   sys_wel
#   sys_wel_bin
#   mount
#   bkgr
#   tskbr
#   ttl
#-----------------------------------#
# this part sets up any thing that needs to be setup before the desktop is loaded

dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# Configure the logging module  
# Configure the logging module  
#logging.basicConfig(filename=f'error{dt}.log', level=logging.ERROR) this is the error log, it will log any errors that happen in the desktop module, the other modules have their own error logs

SYST = 'sys'
system = 'system'
home_dir = 'system/home/user'
SYS_BIN = 'system/bin'
SYS_SCRIPTS = 'system/scripts'
sys_addr = 'system/addons'
sys_docu = 'system/documents'
sys_hom_usr_desk = 'system/home/user/desktop'
sys_hom_usr_doc = 'system/home/user/documents'
sys_hom_usr_doc_pro = 'system/home/user/documents/projects'
sys_logs = 'system/logs'
sys_wel = 'system/welcome'
sys_wel_bin = 'system/welcome/bin'
mount = 'mount'
user = os.getlogin() # get the username of the user on a windows, linux, or mac computer
#-----------------------------------#
#----------------------------------#
#   config.ini
#   this is the config file for the desktop
#   it is used to set the desktop's background color, taskbar color, and more!
#----------------------------------#
if os.path.isfile('python/config.ini'):# check if the config file exists
    try:
        # if it does, load it
        config = configparser.ConfigParser()# get the config thing setup
        config.read('python/config.ini')# read the config file to set the desktop! 
        # if you want to change the background color or something, modify config.ini
        bkgr = config.get('desktop', 'background')
        tskbr = config.get('desktop', 'taskbar')
        ttl = config.get('desktop', 'title')
        geo = config.get('desktop', 'geometry')
        taskbar_height = config.get('taskbar', 'taskbar_height')
        taskbar_color = config.get('taskbar', 'taskbar_color')
        print("Config loaded.")
    except Exception as e:
        
        error = e
        # Log the error message to a file
        #logging.error(str(e)) dont undo this unless you know what your doing and you have free space when debugging, this is important as everytime the desktop is loaded, it will log the error to a file
        # that is why i have it commented out, because it will fill up your hard drive with error logs
        # there is a way to fix this, but i dont know how to do it 
        # there is more of these aswell in the other modules and in here aswell -charlie!

        print("Error loading config.ini. Please check your config.ini file.")
        print("If you do not have a config.ini file, please create one.")
        print("If you do not know how to create a config.ini file, please read the documentation.")
        print("defaluting to built-in confuguration...")
else:
    bkgr = 'darkgray' # if it doesnt, set the desktop to the default color
    tskbr = 'True' # if it doesnt, set the taskbar to the default color
    ttl = 'PythonicOS' # if it doesnt, set the title to the default title
    geo = '800x600' # if it doesnt, set the geometry to the default size
    taskbar_height = '30' # if it doesnt, set the taskbar height to the default height
    taskbar_color = 'black' # if it doesnt, set the taskbar color to the default color
    print("Config not found. Defaluting to built-in confuguration...")



# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='My Script')

# Add an argument for the verbose option
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

# Parse the command-line arguments
args = parser.parse_args()

# Access the value of the verbose option
if args.verbose:
    print("Verbose mode is enabled. Debugging information will be displayed.")

# Rest of your code...


def create_app(root,name):
    root.destroy()
    subprocess.Popen(['python', 'python/bluescreens/pycrashconfig.py', name])
    
def scat():
    print("scat")
#----------------------------------#
time.sleep(1)
print("Loading PythonicOS.")
time.sleep(1)
print("Loading desktop..")
time.sleep(1)
print("Loading desktop modules...")
time.sleep(1)
print(f"Welcome to PythonicOS! {user}")


root.title(ttl)
root.geometry(geo)
if tskbr == 'True':
    try:
        taskbar = tk.Frame(root, height=taskbar_height, bg=taskbar_color)
        taskbar.pack(side=tk.TOP, fill=tk.X)
    except Exception as e:
    # Log the error message to a file
        #logging.error(str(e))
        print("Error loading taskbar. Please check your config.ini file.")
else:
    print("Taskbar disabled. To enable the taskbar, please edit config.ini and set taskbar to True.")
desktop = tk.Frame(root, bg=bkgr)

#----------------------------------#

desktop.pack(expand=True, fill=tk.BOTH)

def epiOS(root):
    print("Thanks for using PythonicOS!")
    root.quit()
# Create a frame for the custom widget
epios = tk.Frame(taskbar, width=100, height=30, bg='blue')

# Add your custom widget content here
label = tk.Button(epios, text='Exit', relief=tk.RAISED, command=lambda: epiOS(root))
label.pack()

# Add the custom widget frame to the taskbar
epios.pack(side=tk.RIGHT)
# Create a frame for the custom widget
epios2 = tk.Frame(taskbar, width=100, height=30, bg='blue')

# Add your custom widget content here
label = tk.Button(epios2, text='crash', relief=tk.RAISED, command=lambda: create_app(root, "PythonicOS"))
label.pack()

# Add the custom widget frame to the taskbar
epios2.pack(side=tk.RIGHT)

epios3 = tk.Frame(taskbar, width=100, height=30, bg='blue')

# Add your custom widget content here
label = tk.Button(epios3, text=dt, relief=tk.RAISED)
label.pack()

# Add the custom widget frame to the taskbar
epios3.pack(side=tk.RIGHT)
#-----------------------#




#---------------------------------#
def start_rename(home_dir, label):
    if args.verbose:
        print("start_rename")
    entry = tk.Entry(label, relief=tk.FLAT)
    entry.insert(0, label.cget("text"))
    entry.bind("<Return>", lambda event, path=home_dir, entry=entry: finish_rename(path, entry))
    entry.bind("<FocusOut>", lambda event, entry=entry: entry.destroy())
    entry.pack()
    entry.select_range(0, tk.END)
    entry.focus()

def finish_rename(home_dir, entry):
    if args.verbose:
        print("finish_rename")
    new_filename = entry.get().strip()
    new_home_dir = os.path.join(os.path.dirname(home_dir), new_filename)

    # Close any open file handles
    entry.destroy()

    # Rename the file
    try:
        os.rename(home_dir, new_home_dir)
        load_files_thread(home_dir)
    except Exception as e:
    # Log the error message to a file
        #logging.error(str(e))
        return
    load_files_thread(home_dir)
    if is_pinned(home_dir):
        unpin_from_taskbar(home_dir)
        pin_to_taskbar(new_home_dir)
    load_files_thread(home_dir)

def delete_file(home_dir):
    if args.verbose:
        print("delete_file")
    load_files_thread(home_dir)
    if os.path.isfile(home_dir):
        os.remove(home_dir)
        load_files_thread(home_dir)
        print(f'{home_dir} has been deleted.')
        load_files_thread(home_dir)



def create_file(home_dir):
    if args.verbose:
        print("create_file")
    # Create the main window
    root = tk.Tk()
    root.title('File Explorer')

    # Create a frame for the directory tree
    tree_frame = tk.Frame(root)
    tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tree_frame.config

    # Create a frame for the file list
    file_frame = tk.Frame(root)
    file_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a label for the current directory
    current_dir_label = tk.Label(tree_frame, text='Current Directory: {}'.format(home_dir))
    current_dir_label.pack(side=tk.TOP, padx=10, pady=10)

    # Create a treeview widget for the directory tree
    treeview = ttk.Treeview(tree_frame)
    treeview.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Add the root node to the treeview
    root_node = treeview.insert('', 'end', text=os.path.basename(home_dir), open=True)

    # Add the child nodes to the root node
    for file in os.listdir(home_dir):
        file_path = os.path.join(home_dir, file)
        if os.path.isdir(file_path):
            treeview.insert(root_node, 'end', text=file, open=False)

    # Create a scrollbar for the treeview
    scrollbar = tk.Scrollbar(tree_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    treeview.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=treeview.yview)

    # Create a listbox widget for the file list
    file_listbox = tk.Listbox(file_frame)
    file_listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Create a scrollbar for the file list
    scrollbar = tk.Scrollbar(file_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    file_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=file_listbox.yview)

    # Create a label for the file name entry
    file_name_label = tk.Label(file_frame, text='File Name:')
    file_name_label.pack(side=tk.TOP, padx=10, pady=10)

    # Create an entry widget for the file name
    file_name_entry = tk.Entry(file_frame)
    file_name_entry.pack(side=tk.TOP, padx=10, pady=10)

    # Create a button to create the file
    create_button = tk.Button(file_frame, text='Create File', command=lambda: create_file_action(home_dir, file_name_entry.get()))
    create_button.pack(side=tk.TOP, padx=10, pady=10)

    # Create a button to close the window
    close_button = tk.Button(file_frame, text='Close', command=root.destroy)
    close_button.pack(side=tk.TOP, padx=10, pady=10)

    # Set the minimum size of the window
    root.minsize(800, 600)

    # Start the main event loop
    root.mainloop()

def create_file_action(home_dir, file_name):
    # Create the file

    filename = '{}.py'.format(file_name)

    with open(os.path.join(home_dir, filename), 'w') as file:
        file.write('This is the content of {}'.format(filename))

    # Reload the file list
    load_files_thread(home_dir)

def show_popup(message):
    popup = tk.Tk()
    popup.wm_title("Popup")
    label = tk.Label(popup, text=message)
    label.pack()
    popup.after(3000, lambda: popup.destroy())  # Close the popup after 3000 milliseconds (3 seconds)
    popup.mainloop()

def show_files_context_menu(event):
    context_menu = tk.Menu(desktop, tearoff=0)

    label = event.widget
    home_dir = os.path.join(os.path.dirname(__file__), 'system/home/user', label.cget("text"))

    if not is_pinned(home_dir):
        context_menu.add_command(label='Pin to Taskbar', command=lambda: pin_to_taskbar(home_dir))
    if is_pinned(home_dir):
        context_menu.add_command(label='Unpin from Taskbar', command=lambda: unpin_from_taskbar(home_dir))
    context_menu.add_command(label='Rename', command=lambda: start_rename(home_dir, label))
    context_menu.add_command(label='Refresh', command=lambda: refresh_code())
    context_menu.add_command(label='Delete', command=lambda: (delete_file(home_dir), load_files_thread(home_dir)))
    context_menu.post(event.x_root, event.y_root)
def open_file_with_path(path):
            open_file(path)
def load_files_thread(home_dir):
    for widget in desktop.winfo_children():
        widget.destroy()


    if not os.path.isdir(home_dir):
            try:
                home_dir = os.path.join(os.path.dirname(__file__), 'system/home/user')
            except Exception as e:
                print(f"Error: {e}")
    else:
        files = sorted(os.listdir(home_dir))  # Sort files alphabetically
        grid_columns = 9
        grid_row = 0
        grid_column = 0

        for file in files:
            file_path = os.path.join(home_dir, file)
            label = tk.Label(desktop, text=file, pady=10)

            # Get the file extension
            _, extension = os.path.splitext(file_path)

            # Set the background color based on the file extension
            if extension == '.cs':
                label.configure(background='darkblue')
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

            grid_column += 1
            if grid_column == grid_columns:
                grid_column = 0
                grid_row += 1
            label.grid(row=grid_row, column=grid_column)


            label.bind("<Button-1>", lambda event, path=file_path: open_file_with_path(path))
            label.bind("<Button-3>", lambda event, path=file_path: show_files_context_menu(event))
            label.grid(row=grid_row, column=grid_column, padx=10, pady=10, sticky='w')

def refresh_code(home_dir):
    load_files_thread(home_dir)

def load_files_threa(home_dir):
    import threading
    # create a new thread to run the load_files() function
    t = threading.Thread(target=load_files_thread(home_dir), args=(home_dir,))
    t.start()

def show_desktop_context_menu(event):
    global file_context_menu
    file_context_menu = tk.Menu(desktop, tearoff=False)
    home_dir = os.path.join(os.path.dirname(__file__), 'system/home/user')

    if not is_pinned(home_dir):
        file_context_menu.add_command(label='Pin to Taskbar', command=lambda: pin_to_taskbar(home_dir))
    if is_pinned(home_dir):
        file_context_menu.add_command(label='Unpin from Taskbar', command=lambda: unpin_from_taskbar(home_dir))

    file_context_menu.add_command(label='New File', command=lambda: create_file(home_dir))
    file_context_menu.add_command(label='Load Files', command=lambda: load_files_thread(home_dir))
    file_context_menu.add_command(label='Refresh', command=lambda: refresh_code(home_dir))
    file_context_menu.add_command(label='Delete', command=lambda: (delete_file(home_dir), load_files_thread(home_dir)))
    file_context_menu.post(event.x_root, event.y_root)

desktop.bind("<Button-3>", show_desktop_context_menu)

def pin_to_taskbar(home_dir):
    if not is_pinned(home_dir):
        taskbar_label = tk.Label(taskbar, text=os.path.basename(home_dir), padx=10)
        taskbar_label.pack(side=tk.LEFT)

        def open_pinned_file(path=home_dir):
            open_file(path)

        taskbar_label.bind("<Button-1>", lambda event: open_pinned_file())
        taskbar_label.bind("<Button-3>", lambda event: show_files_context_menu(event))
        load_files_thread(home_dir)
def open_file(home_dir):
    if home_dir:
        subprocess.Popen(['python', 'system/addons/panno.py', home_dir])
        print(home_dir)
    else:
        print("No file path provided.")

def unpin_from_taskbar(home_dir):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            widget.destroy()

def find_label(home_dir):
    for widget in desktop.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            return widget
def main():
    load_files_thread(home_dir)    
def is_pinned(home_dir):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(home_dir):
            return True
    return False
load_files_threa(home_dir)
print('hello') 

root.mainloop()


if __name__ == ('__main__'):
    main()