import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT")
model_name = os.getenv("MODEL_NAME")
api_version = os.getenv("API_VERSION")

def analizar_productos(productos):
    prompt = f"""
Analiza esta lista de productos scrapeados y dime:
- ¿Cuál es el producto más caro?
- ¿Cuántos productos hay?
- Haz un resumen corto de lo que se ofrece.

Productos: {productos}
"""

    response = openai.ChatCompletion.create(
        engine=model_name,
        api_version=api_version,
        messages=[
            {"role": "system", "content": "Eres un asistente experto en análisis de productos."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]
