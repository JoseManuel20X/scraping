# db_utils.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

# ✅ Cargar variables desde el archivo .env
load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "scraping_llm"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "2106")  
    )

def insertar_producto(titulo, precio, url):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO productos (titulo, precio, url)
        VALUES (%s, %s, %s);
    """, (titulo, precio, url))
    conn.commit()
    cur.close()
    conn.close()

def insertar_archivo(nombre, url, hash_valor):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO archivos (nombre, url, hash)
        VALUES (%s, %s, %s);
    """, (nombre, url, hash_valor))
    conn.commit()
    cur.close()
    conn.close()
