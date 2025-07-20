import requests
from bs4 import BeautifulSoup
import os
import json

URL = "https://books.toscrape.com/"  # Cambiado para usar el sitio de libros
DOWNLOAD_DIR = "downloads"  # No necesario para scraping de productos, pero mantengo si quieres usarlo

def scrape_static_books():
    # Crear carpeta para almacenamiento si es necesario (aunque no la usamos aquí)
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    
    # Realizar request a la página de libros
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    libros = []

    # Buscar todos los libros en la página
    for book in soup.find_all("article", class_="product_pod"):
        try:
            titulo = book.find("h3").find("a")["title"]
            precio = book.find("p", class_="price_color").text
            link = URL + book.find("h3").find("a")["href"]

            libros.append({
                "titulo": titulo,
                "precio": precio,
                "url": link
            })

        except Exception as e:
            print(f"Error en un libro: {e}")
            continue

    # Guardar metadata en JSON
    with open("data/books.json", "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

    print(f"Scraping estático finalizado. Se extrajeron {len(libros)} libros.")

if __name__ == "__main__":
    scrape_static_books()
