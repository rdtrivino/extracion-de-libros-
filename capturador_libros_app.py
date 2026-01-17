import requests
from bs4 import BeautifulSoup
import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def extraer_libros():
    try:
        carpeta = filedialog.askdirectory(
            title="Seleccione la carpeta donde se guardará el archivo CSV"
        )
        if not carpeta:
            return

        archivo_csv = os.path.join(carpeta, "libros_capturados.csv")

        # Conexión
        url = "https://books.toscrape.com/"
        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()

        # Extracción
        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")[:10]

        datos = []

        for book in books:
            titulo = book.h3.a["title"]
            precio_texto = book.select_one("p.price_color").text
            precio = float(re.sub(r"[^\d.]", "", precio_texto))
            datos.append([titulo, precio])

        # Guardar CSV
        with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Título", "Precio"])
            writer.writerows(datos)

        messagebox.showinfo(
            "Proceso finalizado",
            f"La extracción se completó correctamente.\n\n"
            f"Libros guardados: {len(datos)}\n"
            f"Archivo generado:\n{archivo_csv}"
        )

    except Exception as e:
        messagebox.showerror(
            "Error en el proceso",
            f"Ocurrió un problema durante la extracción:\n\n{str(e)}"
        )


def main():
    root = tk.Tk()
    root.title("Extractor de Libros")
    root.geometry("420x220")
    root.resizable(False, False)

    label = tk.Label(
        root,
        text="Extracción de libros desde Books to Scrape",
        font=("Segoe UI", 12)
    )
    label.pack(pady=25)

    boton = tk.Button(
        root,
        text="Extraer libros",
        font=("Segoe UI", 11),
        width=22,
        command=extraer_libros
    )
    boton.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
