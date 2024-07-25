import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.Open(initialdir='/path/to/directory')

print(file_path)
