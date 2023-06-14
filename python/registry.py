import os
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("pysonic registry editor")

# Create the list box
listbox = tk.Listbox(root)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the text view
text = tk.Text(root)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Find all the config files in the same directory as the script
config_files = [f for f in os.listdir() if f.endswith('ini')]

# Add each config file to the list box
for config_file in config_files:
    listbox.insert(tk.END, config_file)

# Allow editing of the file contents when a file is selected
def edit_contents(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        filename = listbox.get(index)
        with open(filename, 'r') as f:
            contents = f.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, contents)

listbox.bind('<<ListboxSelect>>', edit_contents)

# Save the edited contents of a file when the Return key is pressed
def save_contents(event):
    selection = listbox.curselection()
    if selection:
        filename = listbox.get(selection[0])
        contents = text.get('1.0', tk.END)
        with open(filename, 'w') as f:
            f.write(contents)

text.bind('<Control-s>', save_contents)

# Start the main loop
root.mainloop()