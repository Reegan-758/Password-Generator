import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.pack()
        
        self.letters_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        self.letters_check = tk.Checkbutton(root, text="Include Letters", variable=self.letters_var)
        self.letters_check.pack()
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.numbers_var)
        self.numbers_check.pack()
        self.symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.symbols_var)
        self.symbols_check.pack()
        
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()
        
        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()
        self.password_display = tk.Entry(root, state='readonly')
        self.password_display.pack()
        
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            use_letters = self.letters_var.get()
            use_numbers = self.numbers_var.get()
            use_symbols = self.symbols_var.get()
            password = generate_password(length, use_letters, use_numbers, use_symbols)
            self.password_display.config(state='normal')
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_display.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
