1. Descripción del proyecto

Este proyecto consiste en una aplicación de escritorio para Windows, desarrollada en Python, que accede al sitio web de prueba Books to Scrape y realiza la extracción de información de libros.

La aplicación:

Extrae los nombres y precios de los primeros 10 libros

Limpia los precios para convertirlos en valores numéricos

Guarda los datos en un archivo CSV

Muestra mensajes visuales de éxito o error mediante una interfaz gráfica

La solución fue encapsulada en un archivo ejecutable (.exe) para permitir su uso mediante doble clic, sin requerir Python instalado.

2. Funcionalidades principales

Conexión al sitio web: https://books.toscrape.com/

Extracción de los primeros 10 libros de la página principal

Procesamiento del precio eliminando símbolos de moneda

Exportación de resultados a libros_capturados.csv

Interfaz gráfica amigable con selección de carpeta

Mensajes informativos para el usuario

3. Explicación del código

El proyecto está estructurado de la siguiente manera:

Librerías utilizadas

requests: realiza la conexión HTTP al sitio web

BeautifulSoup: analiza el HTML y extrae la información

csv: genera el archivo CSV de salida

tkinter: crea la interfaz gráfica de escritorio

re: limpia el precio usando expresiones regulares

urllib3: gestiona advertencias SSL en el ejecutable

Flujo del programa

El usuario presiona el botón “Extraer libros”

Se solicita seleccionar la carpeta de destino

Se realiza la conexión a la página web

Se obtienen los títulos y precios de los libros

El precio se limpia para dejar solo valores numéricos

Se genera el archivo libros_capturados.csv

Se muestra un mensaje indicando cuántos registros se guardaron

Limpieza del precio (procesamiento)

El precio se procesa usando expresiones regulares para asegurar compatibilidad con diferentes codificaciones:

precio = float(re.sub(r"[^\d.]", "", precio_texto))


Esto elimina cualquier símbolo de moneda y deja solo el valor numérico.

4. Cómo ejecutar la aplicación
Opción 1: Ejecutable (recomendada)

Abrir el archivo:

capturador_libros_app.exe


Presionar “Extraer libros”

Seleccionar la carpeta donde se guardará el CSV

El archivo libros_capturados.csv se genera automáticamente

No requiere Python instalado.

Opción 2: Ejecutar el código Python (opcional)
Requisitos:

Python 3.x

Librerías:

pip install requests beautifulsoup4

Ejecutar:
python capturador_libros_app.py