from odf.opendocument import load
##utilizamos load para cargar un documento ODF
from odf import text, teletype
##importamos dos modulos de la biblioeca odf

archivo = load("word/document.odt")
for bloque in archivo.getElementsByType(text.P):
    ##representa los parrafos del documento
    print(teletype.extractText(bloque))
