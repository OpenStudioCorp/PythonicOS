from tkinter import messagebox
import tkinter as tk

def show_file_context_menu(event, filepath):
    context_menu = tk.Menu(desktop, tearoff=0)

    # Add "Open" option to the right-click menu
    context_menu.add_command(label='Open', command=lambda: open_file(filepath))

    if filepath.endswith('.py'):
        context_menu.add_command(label='Run with Python IDE', command=lambda: run_with_python_ide(filepath))

    if filepath.endswith('.html'):
        context_menu.add_command(label='Open with Browser', command=lambda: open_html_file(filepath))

    context_menu.add_command(label='Rename', command=lambda: start_rename(filepath))
    context_menu.add_command(label='Delete', command=lambda: delete_file(filepath))
    context_menu.post(event.x_root, event.y_root)

def run_with_python_ide(filepath):
    try:
        subprocess.run(['idle', '-r', filepath])
    except FileNotFoundError:
        messagebox.showerror('Run with Python IDE', 'IDLE is not installed on your system.')


def start_rename(filepath):
    label = find_label(filepath)
    entry = tk.Entry(label, relief=tk.FLAT)
    entry.insert(0, os.path.basename(filepath))
    entry.bind("<Return>", lambda event, path=filepath, entry=entry: finish_rename(path, entry))
    entry.bind("<FocusOut>", lambda event, entry=entry: entry.destroy())
    entry.pack()
    entry.select_range(0, tk.END)
    entry.focus()

def finish_rename(filepath, entry):
    new_filename = entry.get().strip()
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)
    os.rename(filepath, new_filepath)
    if is_pinned(filepath):
        unpin_from_taskbar(filepath)
        pin_to_taskbar(new_filepath)
    load_files()

def is_pinned(filepath):
    for widget in taskbar.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            return True
        return False
    
def find_label(filepath):
    for widget in desktop.winfo_children():
        if isinstance(widget, tk.Label) and widget.cget("text") == os.path.basename(filepath):
            return widget

def delete_file(filepath):
   desktop.bind("<Button-3>", lambda event: file_context_menu.delete(0, tk.END))
