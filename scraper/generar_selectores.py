import openai
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_ENDPOINT")
openai.api_type = "azure"
openai.api_version = os.getenv("API_VERSION")

# Nombre del modelo que vamos a usar
MODEL_NAME = os.getenv("MODEL_NAME")

# Función para analizar un producto usando el modelo de OpenAI
def obtener_analisis_producto(producto):
    # Crear un prompt dinámico para el análisis
    prompt = (
        f"Producto analizado:\n"
        f"Nombre: {producto['titulo']}\n"
        f"Precio: {producto['precio']}\n"
        f"Origen: {producto.get('origen', 'Desconocido')}\n\n"
        "¿Qué detalles podemos extraer de este producto?"
    )

    try:
        # Llamar a la API de OpenAI para analizar el producto
        response = openai.ChatCompletion.create(
            engine=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de productos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,  # Variabilidad de la respuesta
            max_tokens=300    # Limitar la longitud de la respuesta
        )

        # Extraer y retornar la respuesta del modelo
        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"❌ Error al obtener análisis del producto: {e}")
        return "Error al analizar el producto"

# Ejemplo de uso de la función de análisis
if __name__ == "__main__":
    # Definir un producto para prueba
    producto = {
        "titulo": "Curso Completo de Python",
        "precio": "49.99",
        "origen": "Estados Unidos"
    }

    # Obtener el análisis generado por la IA
    analisis = obtener_analisis_producto(producto)
    print(f"🧠 Análisis generado por la IA:\n{analisis}")
