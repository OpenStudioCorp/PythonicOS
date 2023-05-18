import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
def apply_syntax_cat(self, language):
        # Remove existing tags
        self.text.tag_remove("syntax", "1.0", tk.END)

        if language == "python":
            # Configure Pygments lexer and formatter
            lexer = PythonLexer()
            formatter = get_formatter_by_name("html", linenos=False)

            # Apply syntax highlighting
            code = self.text.get("1.0", tk.END)
            highlighted_code = pygments.highlight(code, lexer, formatter)

            # Insert the highlighted code
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, highlighted_code, "syntax")

            # Configure the tag for syntax highlighting
            self.text.tag_configure("syntax", font=("Courier New", 10))



class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PANNO!")
        self.text = tk.Text(root)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.undo_stack = []
        self.redo_stack = []
        self.bind_keyboard_shortcuts()
        self.current_file = None  # Variable to store the current file name

        # Create the menu bar
        menu_bar = tk.Menu(root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menu_bar.add_cascade(label="File", menu=file_menu)
        root.config(menu=menu_bar)

        # Create the toolbar
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        load_button = tk.Button(toolbar, text="Load", command=self.load_file)
        load_button.pack(side=tk.LEFT)

        save_button = tk.Button(toolbar, text="Save", command=self.save_file)
        save_button.pack(side=tk.LEFT)

        undo_button = tk.Button(toolbar, text="highlight", command=apply_syntax_cat(self,python))
        undo_button.pack(side=tk.LEFT)

        redo_button = tk.Button(toolbar, text="Redo", command=self.redo)
        redo_button.pack(side=tk.LEFT)

        self.root.bind("<Control-space>", self.complete)

    def bind_keyboard_shortcuts(self):
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-z>", self.undo)
        self.root.bind("<Control-y>", self.redo)

    def load_file(self, event=None):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text.delete("1.0", tk.END)
                    self.text.insert(tk.END, file.read())
                    self.current_file = file_path  # Update the current file name
                    self.update_title()  # Update the title
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def save_file(self, event=None):
        if self.current_file:
            try:
                with open(self.current_file, "w") as file:
                    file.write(self.text.get("1.0", tk.END))
                    messagebox.showinfo("Save", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(self.text.get("1.0", tk.END))
                        self.current_file = file_path  # Update the current file name
                        self.update_title()  # Update the title
                        messagebox.showinfo("Save", "File saved successfully.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def undo(self, event=None):
        if self.undo_stack:
            text = self.undo_stack.pop()
            self.redo_stack.append(self.text.get("1.0", tk.END))
            self.text.delete("1.0",)
            self.text.insert(tk.END, text)

    def redo(self, event=None):
        if self.redo_stack:
            text = self.redo_stack.pop()
            self.undo_stack.append(self.text.get("1.0", tk.END))
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, text)

    def complete(self, event=None):
        # Check if a file is loaded
        if self.current_file:
            file_extension = self.current_file[self.current_file.rfind('.'):]

            completer = self.get_completer(file_extension)

            # Get the current cursor position
            cursor_position = self.text.index(tk.INSERT)

            # Split the code into lines
            lines = self.text.get("1.0", tk.END).split("\n")
            current_line = int(cursor_position.split(".")[0]) - 1

            # Get the code from the current line
            current_code = lines[current_line]

            # Get the code before the cursor position on the current line
            code_before_cursor = current_code[:int(cursor_position.split(".")[1]) - 1]

            # Calculate the starting position of the current code
            start_position = sum(len(line) + 1 for line in lines[:current_line]) + len(code_before_cursor) + 1

            # Set the start and end positions for the prompt_toolkit completion
            completer.position = len(code_before_cursor) + 1
            completer.document = prompt_toolkit.document.Document(code_before_cursor, cursor_position=start_position)

            # Run the prompt_toolkit completion
            completion = prompt("", completer=completer)

            # Insert the completed code at the cursor position
            self.text.insert(tk.INSERT, completion)

    def get_completer(self, file_extension):
        if file_extension == '.py':
            return WordCompleter([
                'print',
                'if',
                'for',
                'while',
                'def',
                'class',
                'import',
                'from',
                'True',
                'False',
                'None',
            ])
        elif file_extension == '.html':
            return WordCompleter([
                'html',
                'head',
                'body',
                'div',
                'p',
                'a',
                'img',
                'table',
                'tr',
                'td',
                'span',
                'style',
                'script',
                'link',
            ])
        elif file_extension == '.css':
            return WordCompleter([
                'color',
                'background-color',
                'font-size',
                'font-family',
                'margin',
                'padding',
                'width',
                'height',
                'border',
                'display',
                'position',
                'float',
                'text-align',
                'border-radius',
                'box-shadow',
            ])
        else:
            return WordCompleter([])  # Default empty completer

    def update_title(self):
        if self.current_file:
            self.root.title(f"Text Editor - {self.current_file}")
        else:
            self.root.title("Text Editor")





if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

