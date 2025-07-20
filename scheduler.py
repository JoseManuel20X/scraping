# Scheduler que ejecuta scraping cada 30 minutos automáticamente

from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import datetime
import logging
import os

# Crear carpeta de logs si no existe
os.makedirs("logs", exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', seconds=30)
def ejecutar_scrapings():
    ahora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Ejecutando scraping a las {ahora}")
    logging.info("Iniciando scraping")

    try:
        print("Ejecutando scraping estático")
        subprocess.run(["python", "scraper/scraper_static.py"], check=True)
        logging.info("Scraping estático completado.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error en scraping estático: {e}")

    try:
        print("Ejecutando scraping dinámico")
        subprocess.run(["python", "scraper/scraper_dynamic.py"], check=True)
        logging.info("Scraping dinámico completado.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error en scraping dinámico: {e}")

    logging.info("Scraping completo.\n")
    print("Scraping completo\n")

print("Iniciando scheduler. si se quiere detener, presione Ctrl+C")
scheduler.start()
