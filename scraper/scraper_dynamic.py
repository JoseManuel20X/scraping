from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import logging
import requests
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# Configurar logs
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Crear carpeta de descargas si no existe
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

def guardar_en_bd(titulo, precio):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO productos (titulo, precio, origen) VALUES (%s, %s, %s)", (titulo, precio, "scraper_dynamic"))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"❌ Error al guardar en BD (dynamic): {e}")

# Crear carpeta de descargas si no existe
def scrape_dynamic():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://books.toscrape.com/")
        time.sleep(3)

        books = driver.find_elements(By.CLASS_NAME, "product_pod")
        for book in books:
            titulo = book.find_element(By.TAG_NAME, "h3").text.strip()
            precio = book.find_element(By.CLASS_NAME, "price_color").text.strip()
            imagen = book.find_element(By.TAG_NAME, "img").get_attribute("src")

            if not imagen.startswith("http"):
                imagen = "https://books.toscrape.com/" + imagen.lstrip('/')

            descargar_imagen(titulo, imagen)
            guardar_en_bd(titulo, precio)

        logging.info("El Scraping dinámico se a completado")
        print("El Scraping dinámico se a completado")
    except Exception as e:
        logging.error(f"Error durante scraping dinámico: {e}")
        print("❌ Error en scraping dinámico:", e)
    finally:
        driver.quit()


if __name__ == "__main__":
    scrape_dynamic()
