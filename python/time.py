import tkinter as tk
import time

def display_clock():
    current_time = time.strftime("%H:%M:%S")

    digits = {
        "0": [" 8888 ",
              "88  88",
              "88  88",
              "88  88",
              " 8888 "],
        "1": ["  88  ",
              " 888  ",
              "  88  ",
              "  88  ",
              "888888"],
        "2": [" 8888 ",
              "    88",
              " 8888 ",
              "88    ",
              "888888"],
        "3": [" 8888 ",
              "    88",
              " 8888 ",
              "    88",
              " 8888 "],
        "4": ["88  88",
              "88  88",
              "888888",
              "    88",
              "    88"],
        "5": ["888888",
              "88    ",
              "8888  ",
              "    88",
              "8888  "],
        "6": [" 8888 ",
              "88    ",
              "8888  ",
              "88  88",
              " 8888 "],
        "7": ["888888",
              "    88",
              "   88 ",
              "  88  ",
              " 88   "],
        "8": [" 8888 ",
              "88  88",
              " 8888 ",
              "88  88",
              " 8888 "],
        "9": [" 8888 ",
              "88  88",
              " 88888",
              "    88",
              " 8888 "],
        ":": ["      ",
              "  ++  ",
              "      ",
              "  ++  ",
              "      "],
        " ": ["      ",
              "      ",
              "      ",
              "      ",
              "      "],
        "AM": ["      ",
               " 8888 ",
               "88  88",
               "88  88",
               "      "],
        "PM": ["      ",
               "88  88",
               "88  88",
               " 8888 ",
               "      "]
    }

    lines = ["", "", "", "", ""]
    for digit in current_time:
        if digit in digits:
            for i, line in enumerate(digits[digit]):
                lines[i] += line + "  "
        else:
            for i in range(5):
                lines[i] += "      "

    time_label.config(text="\n" + "-" * 30 + "\n" + "\n".join(lines) + "\n" + "-" * 30)
    root.after(1000, display_clock)

# Create the tkinter window
root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")
# Create a label to display the time
time_label = tk.Label(root, font=("Courier", 14), justify="center")
time_label.pack()
time_label.configure(bg="grey")
# Start the clock
display_clock()

# Start the tkinter event loop
root.mainloop()
