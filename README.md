Instrucciones de configuración del script del programador (scheduler)
Pasos:
Crea un archivo ./docs/configuración_programador.md con la configuración detallada para ejecutar el scheduler.

## Configuración del Scheduler

1. Instala las dependencias necesarias:
   ```bash
   pip install apscheduler
Ejecute el script para iniciar el scraping cada 30 minutos:

bash
python -m scraper.scraper_dynamic
El scraping se ejecutará de inmediato y luego cada 30 minutos.
