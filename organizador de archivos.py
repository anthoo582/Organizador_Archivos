import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class OrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("organizador de archivos")
        self.resize(350, 250)

        layout = QVBoxLayout()

        self.btn = QPushButton("elegir carpeta")
        self.btn.clicked.connect(self.organize)

        layout.addWidget(self.btn)
        self.setLayout(layout)

    def organize(self):
        folder = input("ingrese la ruta de la carpeta: ")
        if folder:
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

app = QApplication(sys.argv)
window = OrganizerApp()
window.show()
sys.exit(app.exec())
