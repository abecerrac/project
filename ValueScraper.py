import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
import urllib.request as req
import os


# Indicamos la url base para las tablas
urlBase = 'http://www.bolsamadrid.es'

# Y la ubicación de la tabla principal donde se incluyen todas las empresas
extensionTablaBase = '/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
extensionInfoHist = '/esp/aspx/Empresas/InfHistorica.aspx'

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

# Creamos una carpeta para las imagenes:
carpeta = os.getcwd() + "\img\\"

if not os.path.exists(carpeta):
    os.makedirs(carpeta)
    
# Iteramos en todas las empresas de la tabla base
for empresa in tablaBase.find_all("a"):
    # Cogemos el isin de cada empresa (una por cada iteración)
    isin = empresa.get("href")
    isin = isin[-18:]
    # Cogemos el nombre de la empresa
    nombreEmpresa = empresa.get_text()

    # Su URL
    urlEmpresa = urlBase + extensionInfoHist + "/" +isin

    # La página en bruto histórica
    paginaEmpresa = requests.get(urlEmpresa).text
    soup = BeautifulSoup(paginaEmpresa,"lxml")

    # Y cogemos sólo la tabla histórica
    tablaEmpresa = soup.find("table",
                             attrs = {"id":"ctl00_Contenido_tblDatos"})
    # Cogemos también el logo de la empresa:
    urlImgEmpresa = soup.find("th",
                           attrs = {"id":"ctl00_Contenido_CabEmisora_Logo"})
    
    # Cogemos el directorio donde se guarda la imagen
    for img in urlImgEmpresa.find_all("img"):
        dirImgEmpresa = img.get("src")
    # Creamos una variable con la ruta completa   
    rutaImgEmpresa = urlBase+dirImgEmpresa

    # Y guardamos las imágenes en la carpeta correspondiente
    imgEmpresa = req.urlretrieve(rutaImgEmpresa,
                                 filename = carpeta + nombreEmpresa+".gif")

    # Se insera un hipervínculo en el csv. Solo se verá cuando se ponga el
    # texto en columnas. Puede dar errores si el idioma de excel es distinto.
    # Sólo haría falta cambiar el comando.
    hypEmpresa = ("=HIPERVINCULO(\"" + carpeta + nombreEmpresa + ".gif\";" +
                "\"" + nombreEmpresa + "\")")
                
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
                row = (nombreEmpresa,fecha,cierre,maximo,minimo,hypEmpresa)
                # Y lo añadimos a la lista creada anteriormente
                lista.append(row)
                i+=9 # Sumamos 9, el total de columnas de la tabla
            # Miramos la siguiente celda
            numCelda += 1

# Se guarda todo en un dataFrame:
df = pd.DataFrame(lista)

# Dandole nombre adecuado a las columnas. Añadimos la columna Imagen
# aunque tenga el nombre del hipervínculo para que sea más fácil un
# posterior análisis
df.columns = ["Empresa","Fecha","Cierre","Maximo","Minimo","Imagen"]

# Y lo guardamos en un csv:
df.to_csv('AccionesBolsaMadrid.csv', index=False, encoding='utf-8')

# Mostramos un mensaje de finalización:
print("Done!")
            

