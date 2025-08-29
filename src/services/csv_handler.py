"""Helper for persisting scraped data into CSV files."""

from pathlib import Path
from typing import List, Dict
from datetime import datetime

import csv

from src.shared.logger import logger

# Project base directory used to resolve the output folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / "output"


def csv_creator(rows: List[Dict]):
    """Create a CSV file from a list of dictionaries.

    Args:
        rows: List of dictionaries representing table rows.
    """

    logger.info("Creating the CSV")
    # Use the first row to determine the CSV header fields
    fields = rows[0].keys()
    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Ensure the output directory exists before writing
    OUTPUT_DIR.mkdir(exist_ok=True)

    file_name = OUTPUT_DIR / f"inmet_{today}.csv"
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="|")
        w.writeheader()
        # Write all rows into the CSV file
        w.writerows(rows)
    logger.success("CSV was created with success")
