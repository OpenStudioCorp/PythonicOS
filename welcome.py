#!/usr/bin/python3
# write tkinter as Tkinter to be Python 2.x compatible
from tkinter import *
import tkinter as tk
def hello(event):
    print("Single Click, Button-l") 
def show_popup(message):
    popup = tk.Tk()
    popup.wm_title("welcome")
    label = tk.Label(popup, text=message)
    label.pack()
    popup.mainloop()
    
    import sys; sys.exit() 

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', show_popup)
widget.mainloop()