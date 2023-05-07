import tkinter as tk
from tkinter import ttk
import os
import sys
import sysconfig
import desktop
import loginscreen as lsc
from loginscreen import login, login_button, password_label,username_entry,username_label,password_entry
from desktop import load_files,taskbar,taskbar_color,run_with_panno,run_with_pyle,run_with_python_ide,start_rename,finish_rename,refresh_code,desktop_right_click,root,taskbar_height,taskbar_name,pin_to_taskbar,unpin_from_taskbar,create_file,configparser,show_file_context_menu,file_context_menu,file_path,filepath,find_label,open_file,delete_file,open_html_file,home_directory,keyboard,config,script_path,script_path1,script_dir,is_pinned,panno,show_popup,script_path0,app,argparse,QWebEngineView,math,messagebox,desktop,subprocess,sys

def main():
    import configparser
config = configparser.ConfigParser()
config.read('config.ini')
login()


def loggedin(root,GUI,taskbar_height,taskbar_color,taskbar_name,background_color):
    #createe main window when logged in
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

    # Load files onto the desktop
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_files()

    root.mainloop()

    root = tk.Tk()
    root.title("PthonOS")
    root.geometry("640x480")

    taskbar = tk.Frame(root, height=40, bg='lightgrey')
    taskbar.pack(side=tk.TOP, fill=tk.X)

    desktop = tk.Frame(root, bg='grey')
    desktop.pack(expand=True, fill=tk.BOTH)
    desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
    file_context_menu = tk.Menu(root, tearoff=False)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    load_files()
