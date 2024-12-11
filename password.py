import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = ''
    
    if include_uppercase.get():
        characters += string.ascii_uppercase
    if include_lowercase.get():
        characters += string.ascii_lowercase
    if include_numbers.get():
        characters += string.digits
    if include_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()  # now it stays on the clipboard
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

# Password length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Options
include_uppercase = tk.BooleanVar()
include_lowercase = tk.BooleanVar()
include_numbers = tk.BooleanVar()
include_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=include_uppercase).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=include_lowercase).pack()
tk.Checkbutton(root, text="Include Numbers", variable=include_numbers).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=include_special).pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Display Password
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Copy to Clipboard Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Run the application
root.mainloop()
