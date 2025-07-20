import logging
from scraper.scraper_dynamic import scrape_dynamic_site
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def start_scheduler():
    scheduler = BlockingScheduler()

    scheduler.add_job(scrape_dynamic_site, 'interval', minutes=30)
    logger.info("Scheduler iniciado. Scraping se ejecutará cada 30 minutos.")
    scrape_dynamic_site()  
    scheduler.start()

if __name__ == "__main__":
    start_scheduler()
