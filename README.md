# PRÁCTICA 1 WEB SCRAPING

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

  pip install requests

  pip install lxml

  pip install beautifulsoup4

Para ejecutar el script es necesario escrbir el siguiente comando:

***
## 1. Contexto. Explicar en qué contexto se ha recolectado la información. Explique por qué el sitio web elegido proporciona dicha información. 

Debido a que los movimiento de bolsa cambian a diario, es incompatible copiar y pegar los datos a mano, por ello, creemos que una buena fuente de información que fluctúe continuamente como lo hace la bolsa de Madrid, nos permitirá desarrollar un buen web scrapping.
La página oficial en España para poder observar esta información es la Bolsa de Madrid.

## 2. Definir un título para el dataset. Elegir un título que sea descriptivo. 

Valores de las acciones de las empresas de bolsamadrid

## 3. Descripción del dataset. Desarrollar una descripción breve del conjunto de datos que se ha extraído (es necesario que esta descripción tenga sentido con el título elegido). 

El dataset se compone de todas las empresas que cotizan en bolsa presentes en la dirección web http://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?mercado=MC con su diferencia porcentual respecto al cierre anterior, precios de cierre, máximos y mínimos diarios. 

## 4. Representación gráfica. Presentar una imagen o esquema que identifique el dataset visualmente 

https://github.com/abecerrac/project/blob/master/Dataset%20image%20PRAC1.png

## 5. Contenido. Explicar los campos que incluye el dataset, el periodo de tiempo de los datos y cómo se ha recogido. 

El dataset cuenta con las siguientes columnas: diferencia, precioCierre, maxDiario, minDiario y fecha.
Tiene un total de XXXX registros que se han recogido: xxxx
Luego miramos en qué fecha se han escogido los datos.

## 6. Agradecimientos. Presentar al propietario del conjunto de datos. Es necesario incluir citas de investigación o análisis anteriores (si los hay). 

El propietario de los datos es la empresa Bancos y Mercados Españoles, este es el operador de todos los mercados de valores y sistemas financieros de España.

## 7. Inspiración. Explique por qué es interesante este conjunto de datos y qué preguntas se pretenden responder. 

La elección de este conjunto de datos se ha inspirado en la obtención de los valores más representativos de las empresas presentes en la web de bolsamadrid. Con estos datos se pretende tener un archivo con los valores históricos con los que se podrán hacer operaciones y obtener datos como por ejemplo la amplitud de movimiento del precio de las empresas en un el intervalo diario.

## 8. Licencia. Seleccione una de estas licencias para su dataset y explique el motivo de su selección: 

