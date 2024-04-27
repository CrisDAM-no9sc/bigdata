import os

elementos = os.listdir("txt")

for elemento in elementos:
    archivo = open("txt/" + elemento)  
    print(archivo.read())
    archivo.close()  
