from src.services.web_scrapping import Scrapping
from src.services.csv_handler import csv_creator

if __name__ == '__main__':
    rows = Scrapping().run()
    csv_creator(rows)
