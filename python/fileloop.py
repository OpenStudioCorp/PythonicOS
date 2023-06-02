import curses

def draw_desktop(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Desktop")
    stdscr.addstr(2, 1, "[File1] Document.txt")
    stdscr.addstr(3, 1, "[File2] Picture.jpg")
    stdscr.addstr(4, 1, "[File3] Music.mp3")
    stdscr.addstr(5, 1, "[File4] Video.mp4")
    stdscr.addstr(7, 0, "Press 'q' to quit.")

    stdscr.refresh()

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        draw_desktop(stdscr)
        while True:
            key = stdscr.getch()
            if key == ord('q'):
                break

    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

if __name__ == '__main__':
    main()
