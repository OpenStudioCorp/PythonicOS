import time
import os
import time
import os
import sys

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def kbhit():
    # Check if a key is pressed
    if os.name == 'nt':
        import msvcrt
        return msvcrt.kbhit()
    else:
        import termios
        import fcntl
        import select
        # Set stdin file descriptor to non-blocking mode
        fd = sys.stdin.fileno()
        old_attr = termios.tcgetattr(fd)
        new_attr = old_attr[:]
        new_attr[3] = new_attr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, new_attr)
        old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, old_flags | os.O_NONBLOCK)

        try:
            # Check if there is any input available
            _, _, _ = select.select([sys.stdin], [], [], 0)
            return True
        except:
            return False
        finally:
            # Restore stdin back to blocking mode
            termios.tcsetattr(fd, termios.TCSAFLUSH, old_attr)
            fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)

def display_clock():
    while True:
        # Clear the screen before displaying the time
        clear_screen()
        # Get the current time
        current_time = time.strftime("%H:%M:%S")

        # ASCII art digits for each number
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


# Display the time
        lines = ["", "", "", "", ""]
        for digit in current_time:
            if digit in digits:
                for i, line in enumerate(digits[digit]):
                    lines[i] += line + "  "
            else:
                for i in range(5):
                    lines[i] += "      "

        # Print the time in the center of the screen
        print("\n" + "-" * 30)
        for line in lines:
            print(line)
        print("-" * 30)



        # Check if the user pressed the 'Q' key
        if kbhit():
            key = sys.stdin.read(1).upper()
            if key == 'Q':
                break

        # Wait for 1 second
        time.sleep(1)

# Run the clock
display_clock()