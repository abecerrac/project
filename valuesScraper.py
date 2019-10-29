import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd

# Indicamos la url base para las tablas
urlBase = 'http://www.bolsamadrid.es/'

# Y la ubicación de la tabla principal donde se incluyen todas las empresas
extensionTablaBase = 'esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
extensionInfoHist = 'esp/aspx/Empresas/InfHistorica.aspx'

# Y creamos la url de la tabla base:
urlTablaBase = urlBase + extensionTablaBase

page = requests.get(urlTablaBase).text
soup = BeautifulSoup(page,"lxml")

# Obtenemos la tabla enetra
tablaBase = soup.find("table",attrs = {"id":"ctl00_Contenido_tblAcciones"})

# Inicializamos variables
name=""
price=""
nroFila=0
i = 0

# Iteramos en todas las empresas de la tabla base
for empresa in tablaBase.find_all("a"):
    # Cogemos el isin de cada empresa (una por cada iteración)
    isin = empresa.get("href")
    isin = isin[-18:]
    # Cogemos el nombre de la empresa
    nombreEmpresa = empresa.get_text()

    # Su URL
    urlEmpresa = urlBase + extensionInfoHist + isin

    # La página en bruto histórica
    paginaEmpresa = requests.get(urlEmpresa).text
    soup = BeautifulSoup(paginaEmpresa,"lxml")

    # Y cogemos sólo la tabla histórica
    tablaEmpresa = soup.find("table",
                             attrs = {"id":"ctl00_Contenido_tblDatos"})

# Hacemos la iteración para sacar los valores como en el ejemplo
    numCelda = 0
    i = 0
    lista = []
    for fila in tablaEmpresa.find_all("tr"):
        for valor in tablaEmpresa.find_all("td"):
            if numCelda == 0+i:
                fecha = valor.text
            elif numCelda == 1+i:
                cierre = valor.text
            elif numCelda == 6+i:
                maximo = valor.text
            elif numCelda == 7+i:
                minimo = valor.text
                
# Cuando llegamos a la variable 7, sumamos 9 para empezar en la
# siguiente fila ya que la tabla sigue sumando las id:
            if(numCelda > 7+i):
                # Almacenamos todas las variables en una vector
                row = (nombreEmpresa,fecha,cierre,maximo,minimo)
                # Y lo añadimos a la lista creada anteriormente
                lista.append(row)
                i+=9 # Sumamos 9, el total de columnas de la tabla
            # Miramos la siguiente celda
            numCelda += 1

# Se guarda todo en un dataFrame:
df = pd.DataFrame(lista)

# Dandole nombre adecuado a las columnas
df.columns = ["Empresa","Fecha","Cierre","Maximo","Minimo"]

# Y lo guardamos en un csv:
df.to_csv('AccionesBolsaMadrid.csv', index=False, encoding='utf-8')
