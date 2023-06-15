import requests
import json
import tkinter as tk
import subprocess

def install(link):
    # Add your download and install code here
    print(f"Downloading and installing {link}")
    try:
        subprocess.Popen(f"git clone {link}", shell=True)
    except Exception as e:
        print(f"Error: {e}")
        
url = 'http://127.0.0.1:5500/repo.json'
response = requests.get(url)
data = json.loads(response.content)

root = tk.Tk()

lb = tk.Listbox(root)
lb.config(width=50, height=20)
for package in data['packages']:
    name = package['name']
    lb.insert(tk.END, name)

def download_selected():
    selected_name = lb.get(lb.curselection())
    selected_package = next((p for p in data['packages'] if p['name'] == selected_name), None)
    if selected_package:
        install(selected_package['link'])

lb.pack()

button = tk.Button(root, text="Download and Install", command=download_selected)
button.pack()

root.mainloop()