import pdfplumber

archivo = pdfplumber.open("pdf/prueba.pdf")
for pagina in archivo.pages:  
    print(pagina.extract_text())
