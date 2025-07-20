# Este archivo utiliza Azure OpenAI para generar selectores dinámicos
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = os.getenv("API_VERSION")

MODEL_NAME = os.getenv("MODEL_NAME")

def analizar_producto(producto):
    prompt = f"""


Producto:
Título: {producto['titulo']}
Precio: {producto['precio']}
"""

    try:
        response = openai.ChatCompletion.create(
            engine=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Eres un experto en productos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )

        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ Error al analizar producto: {e}")
        return "Error en análisis"

# Ejemplo de prueba local
if __name__ == "__main__":
    producto = {
        "titulo": "Libro de Python Avanzado",
        "precio": "29.99",
        "origen": "España"
    }
    resultado = analizar_producto(producto)
    print("🧠 Análisis generado por la IA:\n", resultado)



    
