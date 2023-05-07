import tkinter as tk
import pygame
from tkinter import filedialog

class AudioPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Audio Player")

        # Create the GUI elements
        self.label = tk.Label(master, text="Select an audio file to play:")
        self.label.pack()

        self.file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.file_button.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(master, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

        # Initialize the Pygame mixer
        pygame.mixer.init()

    def select_file(self):
        # Prompt the user to select an audio file
        file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=(("WAV files", "*.wav"), ("OGG files", "*.ogg"),("mp3 files", "*.mp3")))

        # Update the label with the selected file name
        if file_path:
            self.label.configure(text=f"Selected file: {file_path}")
            self.file_path = file_path

    def play(self):
        # Play the selected audio file
        if hasattr(self, 'file_path'):
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def pause(self):
        # Pause the currently playing audio file
        pygame.mixer.music.pause()

    def stop(self):
        # Stop the currently playing audio file
        pygame.mixer.music.stop()

root = tk.Tk()
app = AudioPlayer(root)
root.mainloop()
