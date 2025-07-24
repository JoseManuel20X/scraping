from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import logging
import requests
from dotenv import load_dotenv
import psycopg2

# Cargar las variables de entorno
load_dotenv()

# Configurar logs
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Función para conectar a la base de datos
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        return conn
    except Exception as e:
        logging.error(f"❌ Error de conexión a la base de datos: {e}")
        print(f"❌ Error de conexión a la base de datos: {e}")
        raise

# Crear la base de datos y la tabla si no existen
def create_db_and_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Verificar si la base de datos existe, si no, crearla
        cur.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{os.getenv('DB_NAME')}';")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {os.getenv('DB_NAME')};")
            conn.commit()
            print(f"✅ Base de datos {os.getenv('DB_NAME')} creada.")
        else:
            print(f"✅ Base de datos {os.getenv('DB_NAME')} ya existe.")
        
        # Ahora que sabemos que la base de datos está creada, verificamos la tabla
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
        logging.info("✅ Tabla 'productos' creada/verificada.")
    except Exception as e:
        logging.error(f"❌ Error al crear la base de datos o la tabla: {e}")
        print(f"❌ Error al crear la base de datos o la tabla: {e}")

# Función para descargar imágenes
def descargar_imagen(titulo, url_imagen):
    try:
        if not url_imagen.startswith("http"):
            url_imagen = "https://books.toscrape.com/" + url_imagen.lstrip('/')
        response = requests.get(url_imagen)
        if response.status_code == 200:
            nombre_archivo = f"downloads/{titulo}.jpg"
            with open(nombre_archivo, "wb") as f:
                f.write(response.content)
        else:
            logging.warning(f"No se pudo descargar imagen de {titulo}: Código {response.status_code}")
    except Exception as e:
        logging.warning(f"No se pudo descargar la imagen de {titulo}: {e}")

# Función para guardar los datos en la base de datos
def guardar_en_bd(titulo, precio, link):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO productos (titulo, precio, url) 
        VALUES (%s, %s, %s)
        """, (titulo, precio, link))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"❌ Error al guardar en BD (dynamic): {e}")

# Función principal de scraping dinámico
def scrape_dynamic():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://books.toscrape.com/")
        time.sleep(3)

        # Buscar productos en la página
        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        for book in books:
            titulo = book.find_element(By.TAG_NAME, "h3").text.strip()
            precio = book.find_element(By.CLASS_NAME, "price_color").text.strip()
            imagen = book.find_element(By.TAG_NAME, "img").get_attribute("src")

            # Descargar imagen
            if not imagen.startswith("http"):
                imagen = "https://books.toscrape.com/" + imagen.lstrip('/')

            descargar_imagen(titulo, imagen)
            guardar_en_bd(titulo, precio, imagen)

        logging.info("✅ El Scraping dinámico se ha completado.")
        print("✅ El Scraping dinámico se ha completado.")
    except Exception as e:
        logging.error(f"❌ Error durante scraping dinámico: {e}")
        print("❌ Error en scraping dinámico:", e)
    finally:
        driver.quit()

# Ejecución principal
if __name__ == "__main__":
    create_db_and_table()  # Crear base de datos y tabla si no existe
    scrape_dynamic()  # Ejecutar el scraping
