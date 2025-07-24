import requests
from bs4 import BeautifulSoup
import os
import json
import psycopg2
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Variables de conexión a la base de datos
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# URL para scraping
URL = "https://books.toscrape.com/"

# Crear carpeta de descargas si no existe
DOWNLOAD_DIR = "downloads"  # No necesario para scraping de productos, pero mantengo si quieres usarlo
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Función para conectar a la base de datos
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        raise

# Crear base de datos y tabla si no existe
def create_db_and_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Crear base de datos si no existe
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}';")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {DB_NAME};")
            conn.commit()
            print(f"✅ Base de datos {DB_NAME} creada.")
        else:
            print(f"✅ Base de datos {DB_NAME} ya existe.")
        
        # Conectar a la base de datos
        conn.close()
        conn = get_db_connection()
        cur = conn.cursor()

        # Crear la tabla de productos si no existe
        cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            titulo TEXT NOT NULL,
            precio TEXT NOT NULL,
            url TEXT NOT NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Tabla 'productos' verificada/creada.")
    except Exception as e:
        print(f"❌ Error al crear la base de datos o la tabla: {e}")

# Función para guardar los libros en la base de datos
def save_books_to_db(libros):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        for book in libros:
            cur.execute("""
            INSERT INTO productos (titulo, precio, url) 
            VALUES (%s, %s, %s)
            """, (book["titulo"], book["precio"], book["url"]))
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Datos guardados en PostgreSQL con éxito.")
    except Exception as e:
        print(f"❌ Error al guardar datos en la base de datos: {e}")

# Función para realizar el scraping de libros
def scrape_static_books():
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

    # Guardar los datos de los libros en la base de datos
    save_books_to_db(libros)

    # Guardar metadata en JSON
    with open("data/books.json", "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

    print(f"Scraping estático finalizado. Se extrajeron {len(libros)} libros.")

if __name__ == "__main__":
    create_db_and_table()  # Crear base de datos y tabla si no existe
    scrape_static_books()  # Ejecutar el scraping
