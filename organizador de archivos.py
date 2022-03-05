import os
import shutil

folder = input("ingrese la ruta de la carpeta: ")

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

print("archivos organizados")
