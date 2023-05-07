import tkinter as tk
import configparser
import os
def main():
    print('welcome to pythonOS!')
    
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Read passwords from configuration file
    config_file = os.path.join(os.path.dirname(__file__), 'pass.ini')
    config = configparser.ConfigParser()
    config.read(config_file)
    print(config.sections())  # Debugging line
    print(config.options('login'))  # Debugging line
    # Check if entered username and password match the ones in the configuration file
    if username in config['login'] and config['login'][username] == password:
        print("Login successful!")
    else:
        print("Incorrect username or password.")
    password_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title('Login')

# Create login form
username_label = tk.Label(root, text='Username')
username_entry = tk.Entry(root)
password_label = tk.Label(root, text='Password')
password_entry = tk.Entry(root, show='*')
login_button = tk.Button(root, text='Login', command=login)

# Add widgets to the window
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()

# Run the main event loop
root.mainloop()
