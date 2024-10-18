import tkinter as tk
from tkinter import filedialog, messagebox
from config import WINDOW_TITLE, WINDOW_SIZE
from utils.file_utils import organize_files

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_SIZE)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Select a folder to organize files:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=20)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            try:
                organize_files(folder_selected)
                messagebox.showinfo("Success", "Files organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
