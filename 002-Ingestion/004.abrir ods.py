import pandas as pd

archivo = pd.read_excel("xlsx/clientes.ods",engine="odf")
print(archivo)
