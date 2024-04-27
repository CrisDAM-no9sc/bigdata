import os

elementos = os.listdir("text")

for elementos in elementos:
    archivo = open("txt/"+elemento)
    print(archivo.read())
