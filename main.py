"""Main module for running the web scraping workflow.

This script orchestrates the scraping process and saves the collected
data into a CSV file for later analysis.
"""

from src.services.web_scrapping import Scrapping
from src.services.csv_handler import csv_creator
from src.shared.logger import logger

if __name__ == "__main__":
    try:
        # Run the scraping process and collect rows of data
        rows = Scrapping().run()
        # Persist the collected data to disk as a CSV
        csv_creator(rows)
        logger.success("Automation Finished")
    except Exception as e:
        logger.exception("Failed runing btime_scrapping")
