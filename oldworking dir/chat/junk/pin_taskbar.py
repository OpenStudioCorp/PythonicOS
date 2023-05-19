import tkinter as tk
from tkinter import messagebox
import subprocess
import os

def pin_to_taskbar(filepath):
    if not is_pinned(filepath):
        taskbar_label = tk.Label(taskbar, text=os.path.basename(filepath), padx=10)
        taskbar_label.pack(side=tk.LEFT)

        def open_pinned_file():
            subprocess.call(['nano', filepath])

        taskbar_label.bind("<Button-1>", lambda event, path=filepath: open_pinned_file())
        taskbar_label.bind("<Button-3>", lambda event, path=filepath: show_file_context_menu(event, path))

def unpin_from_taskbar(filepath):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            widget.destroy()
