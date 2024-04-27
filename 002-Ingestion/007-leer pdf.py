import PyPDF2

archivo = PyPDF2.PdfReader("pdf/prueba.pdf")

paginas = len(archivo.pages)
print(paginas)

for pagina in range(0,paginas):
    actual = archivo.pages[0]
    print(actual.extractText)
