import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel

class OrganizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("anthony organizador de archivos 2022")
        self.resize(350, 250)
        
        layout = QVBoxLayout()
        self.title_label = QLabel("organizador de archivos")
        self.desc_label = QLabel("seleccione alguna carpeta para organizar los archivos")
        self.info_label = QLabel("los archivos se ordenaran dependiendo de la carpeta que seleccione")
        self.status_label = QLabel("estado: esperando seleccion de carpeta")
        self.folder_label = QLabel("carpeta seleccionada: ninguna")
        
        self.btn = QPushButton("elegir carpeta")
        self.btn.clicked.connect(self.organize)
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.desc_label)
        layout.addWidget(self.info_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.folder_label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def organize(self):
        folder = QFileDialog.getExistingDirectory(self, "seleccionar carpeta")
        if folder:
            self.folder_label.setText(f"carpeta seleccionada: {folder}")
            self.status_label.setText("estado: organizando archivos...")
            
            extensions = {
                'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.ico'],
                'documentos': ['.pdf', '.docx', '.txt', '.doc', '.xlsx', '.pptx'],
                'instaladores': ['.exe', '.msi'],
                'comprimidos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'musica': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma']
            }
            
            for file in os.listdir(folder):
                file_path = os.path.join(folder, file)
                if os.path.isfile(file_path):
                    name, ext = os.path.splitext(file)
                    ext = ext.lower()
                    
                    if ext == '.lnk':
                        continue
                    
                    category = 'archivos'
                    for cat, exts in extensions.items():
                        if ext in exts:
                            category = cat
                            break
                    
                    dest_dir = os.path.join(folder, category)
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_dir, file))
            
            self.status_label.setText("estado: organizacion completada")

app = QApplication(sys.argv)
window = OrganizerApp()
window.show()
sys.exit(app.exec())