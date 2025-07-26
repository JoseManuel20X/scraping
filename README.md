Un sistema completo de web scraping para extraer información de libros de Books to Scrape, con almacenamiento en PostgreSQL y API REST para consulta de datos.

🚀 Características

Scraping Estático: Extracción rápida usando requests y BeautifulSoup
Scraping Dinámico: Navegación completa con Selenium para contenido JavaScript
Descarga de Imágenes: Almacenamiento automático de portadas de libros
Base de Datos: Persistencia en PostgreSQL con estructura normalizada
API REST: Endpoints para consultar datos extraídos
Programación Automática: Ejecución periódica con APScheduler
Logging Completo: Registro detallado de operaciones y errores
Exportación JSON: Respaldo de datos en formato JSON

🛠️ Tecnologías Utilizadas
TecnologíaVersiónPropósitoPython3.8+Lenguaje principalPostgreSQL13+Base de datosSelenium4.0+Scraping dinámicoBeautifulSoup44.9+Parsing HTMLFlask2.0+API RESTAPScheduler3.8+Programación de tareasRequests2.25+HTTP requestsPsycopg22.8+Conector PostgreSQL
📦 Instalación
Prerrequisitos

Python 3.8 o superior
PostgreSQL 13 o superior
Google Chrome (para scraping dinámico)
ChromeDriver

1. Clonar el repositorio
bashgit clone https://github.com/tu-usuario/books-web-scraper.git
cd books-web-scraper
2. Crear entorno virtual
bashpython -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. Instalar dependencias
bashpip install -r requirements.txt
4. Configurar variables de entorno
Crear archivo .env en la raíz del proyecto:
env# Configuración de Base de Datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=books_scraper
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña

# Configuración de Scraping
DOWNLOAD_FOLDER=downloads
LOG_LEVEL=INFO
5. Configurar base de datos
bash# Crear base de datos (opcional, se crea automáticamente)
createdb books_scraper
🎯 Uso
Scraping Manual
Scraping Estático (Rápido)
bashpython scraper_static.py
Scraping Dinámico (Completo con imágenes)
bashpython scraper_dynamic.py
Programación Automática
bashpython scheduler.py
El scheduler ejecutará ambos scrapers cada 30 minutos automáticamente.
API REST
bashpython json_api_server.py
La API estará disponible en http://localhost:5000
Endpoints disponibles:
EndpointMétodoDescripción/api/productosGETObtener todos los libros/api/archivosGETObtener archivos descargados
Ejemplo de respuesta:
json{
  "productos": [
    {
      "id": 1,
      "titulo": "A Light in the Attic",
      "precio": "£51.77",
      "url": "downloads/image_001.jpg",
      "fecha_registro": "2025-01-15T10:30:00"
    }
  ]
}
