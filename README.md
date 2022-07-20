# Organizador de Archivos

Aplicación de escritorio para organizar archivos automáticamente por tipo.

## Como usar

1. Ejecutar el script con Python
2. Hacer clic en "Elegir carpeta"
3. Seleccionar la carpeta con archivos desordenados
4. Los archivos se organizarán automáticamente

## Categorías de archivos

| Carpeta | Extensiones |
|---------|-------------|
| Imagenes | jpg, jpeg, png, gif, bmp, webp, ico |
| Documentos | pdf, docx, txt, doc, xlsx, pptx |
| Instaladores | exe, msi |
| Comprimidos | zip, rar, 7z, tar, gz |
| Musica | mp3, wav, flac, aac, ogg, m4a, wma |
| Archivos | Todo lo demás |

## Notas importantes

- Los accesos directos (.lnk) no se mueven
- Solo se organizan archivos, las carpetas se ignoran
- Las carpetas se crean automáticamente si no existen

## Requisitos

- Python 3
- PyQt6 (`pip install pyqt6`)
