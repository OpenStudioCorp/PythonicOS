import subprocess
from tkinter import messagebox
from file import pyle,panno,home_dir
def run_with_python_ide(home_di):
    try:
        subprocess.Popen(['idle', '-r', 'home_dir'])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system!.')


def run_with_pyle(home_di):
    try:
        subprocess.Popen(['python', pyle], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(home_file):
    try:
        subprocess.Popen(['python', panno], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')

def open_file(home_dir):
    try:
        if home_dir.endswith('.cs'):
            subprocess.Popen(['notepad', home_dir])
        elif home_dir.endswith('.html'):
            run_with_panno([home_dir])
        elif home_dir.endswith('.txt'):
            run_with_panno([home_dir])
        else:
            subprocess.Popen(['notepad', home_dir])
    except FileNotFoundError:
        messagebox.showerror('Open File', 'Default program not found for the file extension.')
        
        