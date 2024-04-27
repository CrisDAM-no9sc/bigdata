import pytesseract
##reconocimiento optico de caracteres para OCR
from PIL import Image

archivo = Image.open("jpg/texto.jpg")
print(pytesseract.image_to_string(archivo))
#coje la imagen como entrada y la devulve el texto de la imagen
#como una cadena de texto
