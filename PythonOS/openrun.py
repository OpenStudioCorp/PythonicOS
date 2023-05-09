import subprocess
from tkinter import messagebox
import PythonOS.file as file
def run_with_python_ide(filepath):
    try:
        subprocess.Popen(['idle', '-r', 'filepath'])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system!.')


def run_with_pyle(filepath):
    try:
        subprocess.Popen(['python', pyle], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with pyle', 'pyle is not installed into the /assets folder!.')


def run_with_panno(home_file):
    try:
        subprocess.Popen(['python', panno], cwd=home_dir)
    except FileNotFoundError:
        messagebox.showerror('Run with Panno', 'panno is not installed into the required folder!.')