Archivo ./docs/ con una guía de inicio
Pasos:
Crea una carpeta ./docs/ en la raíz de tu proyecto.

Agrega un archivo guia_inicio.md con las instrucciones de inicio:

markdown
Copiar
## Guía de inicio

### Instalación de dependencias:
1. Clona el repositorio:
   ```bash
   git clone https://github.com/JoseManuel20X/scraping.git
Instala las dependencias:

bash
Copiar
pip install -r requirements.txt
Configuración de la base de datos:
Configura tu archivo .env con las credenciales de la base de datos.

Asegúrate de tener PostgreSQL corriendo.

Ejecución:
Ejecuta el scraper:

bash
Copiar
python -m scraper.scraper_dynamic
Copiar
