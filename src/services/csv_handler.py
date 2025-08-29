from pathlib import Path
from typing import List, Dict
from datetime import datetime

import csv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
OUTPUT_DIR = BASE_DIR / 'output'


def csv_creator(rows: List[Dict]):

    fields = (rows[0].keys())
    today = datetime.now().strftime("%Y%m%d_%H%M%S")
    OUTPUT_DIR.mkdir(exist_ok=True)

    file_name = OUTPUT_DIR / f"inmet_{today}.csv"
    with open(file_name, 'w', newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="|")
        w.writeheader()
        w.writerows(rows)
