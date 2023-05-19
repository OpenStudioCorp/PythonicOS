import sys
from tkinter import messagebox
import subprocess
from PyQt5.QtWidgets import QApplication  # Import QApplication
from context_menu import show_file_context_menu
from pin_taskbar import pin_to_taskbar, unpin_from_taskbar
app = QApplication(sys.argv)

def open_folder(folder_path):
    subprocess.Popen(['python', 'main.py', folder_path])  # Run the main.py script with the folder path as an argument

def open_file(filepath):
    try:
        if filepath.endswith('.cs'):
            subprocess.run(['notepad', filepath])
        elif filepath.endswith('.html'):
            open_html_file(filepath)
        elif filepath.endswith('.txt'):
            subprocess.run(['notepad', filepath])
        else:
            subprocess.run(['notepad', filepath])
    except FileNotFoundError:
        messagebox.showerror('Open File', 'Default program not found for the file extension.')


def open_html_file(filepath):
    app = QApplication(sys.argv)

    # Create a QWebEngineView instance
    web_view = QWebEngineView()

    # Load the local file
    web_view.load(QUrl.fromLocalFile(filepath))

    # Show the browser window
    web_view.show()

    # Run the application event loop
    sys.exit(app.exec_())
