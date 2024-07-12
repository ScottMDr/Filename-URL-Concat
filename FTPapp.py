import tkinter as tk
from tkinter import filedialog, messagebox
import os

class FolderURLConcatenator:
    
    def __init__(self, master):
    #GUI Front end
        self.master = master
        master.title("Folder URL Concatenator")
        master.geometry("400x300")

        self.label = tk.Label(master, text="Select a folder and enter the static URL:")
        self.label.pack(pady=10)
#URL entry point
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack(pady=5)
        self.url_entry.insert(0, "https://example.com/")
#Folder entry point
        self.select_button = tk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack(pady=10)
#Concatenate function
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            static_url = self.url_entry.get().strip()
            if not static_url.endswith('/'):
                static_url += '/'

            result = []
            for filename in os.listdir(folder_path):
                full_url = static_url + filename
                result.append(full_url)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "\n".join(result))

            messagebox.showinfo("Success", f"Processed {len(result)} files from the selected folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderURLConcatenator(root)
    root.mainloop()