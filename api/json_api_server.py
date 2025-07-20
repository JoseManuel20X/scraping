from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from flask_cors import CORS  # Importamos CORS

load_dotenv()

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "scraping_llm"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "2106")
    )

@app.route('/api/productos', methods=['GET'])
def get_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos;")
    productos = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for producto in productos:
        result.append({
            'id': producto[0],
            'titulo': producto[1],
            'precio': producto[2],
            'url': producto[3],
            'fecha_registro': producto[4]
        })

    return jsonify(result)

@app.route('/api/archivos', methods=['GET'])
def get_archivos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM archivos;")
    archivos = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for archivo in archivos:
        result.append({
            'id': archivo[0],
            'nombre': archivo[1],
            'url': archivo[2],
            'hash': archivo[3],
            'fecha_descarga': archivo[4]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
