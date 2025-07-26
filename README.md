# 📚 **Books Web Scraper** 📚
## Automatización de la extracción de datos de libros

### 📖 **Descripción del Proyecto** 📖

**Books Web Scraper** es una herramienta automatizada para la extracción de datos de libros desde el sitio web **Books to Scrape**. Este proyecto emplea tanto **scraping estático** como **dinámico**, y está diseñado para almacenar la información extraída en una base de datos **PostgreSQL**. Además, ofrece funcionalidades como la descarga automática de imágenes de portadas y una **API REST** para consultar los datos extraídos.

### 🔍 **¿Qué Hace?** 🔍

- **Extracción automática** de datos de libros: título, precio, imagen.
- **Almacenamiento persistente** de los datos en **PostgreSQL**.
- **Descarga automática** de imágenes de las portadas de los libros.
- **API REST** para la consulta y consumo de los datos extraídos.
- **Automatización de tareas** para ejecutar el scraping de manera periódica.
- **Análisis de precios** y catálogos de libros.

### 🛠️ **Tecnologías Utilizadas** 🛠️

#### Backend y Scraping

- **Python 3.8+** - Lenguaje principal del proyecto.
- **Selenium** - Herramienta de automatización para scraping dinámico.
- **BeautifulSoup4** - Librería para parsing HTML en scraping estático.
- **Requests** - Librería para realizar peticiones HTTP.

#### Base de Datos y API

- **PostgreSQL** - Sistema de gestión de base de datos relacional.
- **Psycopg2** - Conector de PostgreSQL para Python.
- **Flask** - Framework para la creación de la API REST.
- **Flask-CORS** - Gestión de CORS en la API.

#### Automatización y Utilidades

- **APScheduler** - Librería para la programación de tareas automáticas.
- **Python-dotenv** - Manejo de variables de entorno.
- **Logging** - Sistema integrado para registro de eventos.

### 🚀 **Instalación y Configuración** 🚀

#### **Prerrequisitos**

- **Python 3.8+**.
- **PostgreSQL 13+**.
- **Google Chrome** (para scraping dinámico).
- **Git**.

#### **Pasos de Instalación**

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/JoseManuel20X/scraping.git
    ```

2. Instalar las dependencias de Python:

    ```bash
    cd scraping
    pip install -r requirements.txt
    ```

3. Configurar las variables de entorno en un archivo `.env`:

    ```bash
    # Archivo .env de ejemplo
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=nombre_bd
    DB_USER=usuario
    DB_PASSWORD=contraseña
    ```

4. **Configurar la base de datos**:

    Asegúrate de tener una base de datos PostgreSQL configurada y creada. El proyecto intentará crear la base de datos y las tablas si no existen.

5. **Ejecutar el scraper dinámico**:

    ```bash
    python scraper_dynamic.py
    ```

6. **Ejecutar el scraper estático**:

    ```bash
    python scraper_static.py
    ```

7. **Ejecutar el scheduler**:

    El scheduler ejecutará ambos scrapers cada 30 minutos. Para iniciar el scheduler:

    ```bash
    python scheduler.py
    ```

8. **Ejecutar el servidor de API**:

    Para iniciar la API REST:

    ```bash
    python json_api_server.py
    ```

    La API estará disponible en `http://localhost:5000`.
