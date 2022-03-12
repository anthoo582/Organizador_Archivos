import tkinter as tk
from tkinter import filedialog
import os
import shutil

def organize():
    folder = filedialog.askdirectory()
    if not folder:
        return

    extensions = {
        'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.ico'],
        'documentos': ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.pptx'],
        'instaladores': ['.exe', '.msi'],
        'comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        name, ext = os.path.splitext(file)

        category = 'archivos'
        for cat, exts in extensions.items():
            if ext in exts:
                category = cat
                break

        dest_dir = os.path.join(folder, category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(file_path, os.path.join(dest_dir, file))

root = tk.Tk()
root.title("organizador de archivos")
root.geometry("300x200")

btn = tk.Button(root, text="elegir carpeta", command=organize)
btn.pack(pady=50)

root.mainloop()
