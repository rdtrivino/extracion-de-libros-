# Prueba técnica – Excel y Python  
**Autor:** Rubén Triviño  

Este repositorio contiene la entrega correspondiente **a la prueba solicitada**, la cual consta de dos partes:
1. Un ejercicio de **análisis de datos en Excel**.
2. Un ejercicio de **extracción de datos en Python**.

Debido a restricciones en el envío por correo electrónico, la entrega se realiza a través de este repositorio.

---

## 1️⃣ Ejercicio en Excel – Análisis de datos

### Objetivo
Realizar la limpieza, análisis y visualización de un archivo de datos de clientes y ventas.

### Actividades realizadas
- Limpieza de registros duplicados utilizando el **email como identificador único**, considerando variaciones en el nombre (ej. *Perez / Peres*).
- Aplicación de formato:
  - **Monto_Compra** → formato moneda  
  - **Fecha** → formato fecha corta
- Creación de una **tabla dinámica** que muestra:
  - Total de ventas por ciudad
  - Promedio de venta por ciudad
- Cálculo del **Bono del 5%** sobre el monto de compra.
- Visualización mediante **gráfico de barras** con **segmentador (slicer) por nombre de cliente**.

### Archivo
- `analisis_ventas.xlsx`

---

## 2️⃣ Ejercicio en Python – Extracción de datos

### Objetivo
Desarrollar una aplicación que extraiga información desde un sitio web y exporte los resultados a un archivo CSV.

### Funcionalidades
- Conexión al sitio: https://books.toscrape.com/
- Extracción de los **nombres y precios de los primeros 10 libros** de la página principal.
- Limpieza del precio para convertirlo a un valor numérico.
- Exportación de los resultados a `libros_capturados.csv`.
- Interfaz gráfica de escritorio desarrollada con **Tkinter**.
- Mensajes visuales de confirmación o error.

### Archivos
- `capturador_libros_app.py` → código fuente en Python  
- `libros_capturados.csv` → archivo generado  
- `capturador_libros_app.exe` → aplicación de escritorio para Windows  

---

## 3️⃣ Ejecución del proyecto

### ▶️ Opción 1: Ejecutable (Windows)
1. Ejecutar `capturador_libros_app.exe`
2. Presionar **“Extraer libros”**
3. Seleccionar la carpeta de destino
4. Se genera automáticamente el archivo `libros_capturados.csv`

> No requiere Python instalado.

---

### ▶️ Opción 2: Ejecutar el código Python
#### Requisitos
- Python 3.x
- Librerías:
  ```bash
  pip install requests beautifulsoup4
# Prueba técnica – Excel y Python  
**Autor:** Rubén Triviño  

Este repositorio contiene la entrega correspondiente **a la prueba solicitada**, la cual consta de dos partes:
1. Un ejercicio de **análisis de datos en Excel**.
2. Un ejercicio de **extracción de datos en Python**.

Debido a restricciones en el envío de archivos por correo electrónico, la entrega completa se encuentra disponible en este repositorio GitHub.

---

## 📥 Cómo descargar la entrega

### Opción 1: Descargar todo el repositorio (recomendada)
1. Ingresar a este repositorio en GitHub.
2. Hacer clic en el botón **Code** (verde).
3. Seleccionar **Download ZIP**.
4. Descomprimir el archivo descargado en su equipo.

Una vez descomprimido, tendrá acceso a todos los archivos de la prueba.

---

### Opción 2: Clonar el repositorio (opcional)
Si cuenta con Git instalado, puede clonar el repositorio con el siguiente comando:

```bash
git clone https://github.com/rdtrivino/extracion-de-libros-.git
