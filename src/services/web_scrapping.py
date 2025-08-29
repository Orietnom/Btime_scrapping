"""Service module responsible for scraping weather data from INMET."""

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Page, expect
from typing import List, Dict

import os

from src.shared.logger import logger
from src.shared.date_to_filter import date_to_filter

load_dotenv()


class Scrapping:
    """Encapsulates the steps required to collect data from the site."""

    def __init__(self):
        self.url = os.getenv("URL", "https://tempo.inmet.gov.br/")
        self.product = os.getenv("PRODUCT", "Condições de Tempo Registradas nas Capitais")
        self.days_before = os.getenv("DAYS_BEFORE", 0)
        self.page = self._setup_playwright()

    @staticmethod
    def _setup_playwright() -> Page:
        """Launch a Chromium browser and return a new page instance."""

        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome"
        )

        context = browser.new_context()
        page = context.new_page()
        return page

    def navigate_to_url(self):
        """Navigate to the target URL and wait for the page to load."""
        logger.info(f"Navigating to {self.url}")
        self.page.goto(self.url)
        self.page.wait_for_load_state('load')
        logger.info("Page loaded")

    def filter_and_generate_table(self):
        """Select filters on the page and generate the results table."""

        logger.info("Filtering weather data")
        # Placeholder variables for the elements we need to interact with
        menu = None
        option = None
        generate_table_btn = None

        logger.info("Searching for the product dropdown.")
        comboboxs = self.page.get_by_role("combobox")
        if not comboboxs:
            logger.error("The product dropdown menu not found")
            raise Exception

        for i in range(comboboxs.count()):
            if self.product.lower() in comboboxs.nth(i).text_content().lower():
                menu = comboboxs.nth(i)
                break

        if not menu:
            logger.error("The product dropdown menu was not found")
        # Open the product dropdown
        menu.click()
        logger.info("Product dropdown found and clicked")

        logger.info(f"Searching for product option {self.product}")
        # Choose the desired product option
        product_option = self.page.get_by_text(self.product)
        for i in range(product_option.count()):
            if self.product.lower() in product_option.nth(i).text_content().lower():
                option = product_option.nth(i)
                break

        if not menu:
            logger.error("The product dropdown menu not found")
            raise Exception
        option.click()
        logger.info("Product option found and selected")

        logger.info("Searching for date field")
        # Locate the date input field and type the filter date
        date_field = self.page.locator("input[type='date']")
        if not date_field.count() or date_field.count() > 1:
            logger.error("Date field not found")
            raise Exception

        date_field.nth(0).type(date_to_filter(self.days_before))
        logger.info(f"Date field found and set to {self.days_before}")

        logger.info("Looking for generate table button")
        generate_table_element = self.page.get_by_role("button")

        # Find the button responsible for generating the table
        for i in range(generate_table_element.count()):
            if "gerar tabela" in generate_table_element.nth(i).text_content().lower():
                generate_table_btn = generate_table_element.nth(i)
                break

        if not generate_table_btn:
            logger.error("The generate table button was not found")
            raise Exception

        generate_table_btn.click()
        logger.info("Generate table button found and clicked")

    def get_table(self) -> List[Dict]:
        """Collect the generated table and return its data as dictionaries.

            Returns:
                List[Dict]: Rows of the table
        """

        logger.info("Getting the data about weather")
        # Locate the table and ensure at least one row is present
        table = self.page.locator("table")
        expect(table.locator("tbody tr").first).to_have_count(1, timeout=15000)
        if not table:
            logger.error("The table was not generated")

        logger.info("Getting the table headers")
        # Extract table headers
        headers = [h.inner_text().strip() for h in table.locator("thead tr th").all()]
        logger.info("Headers was extracted")

        logger.info("Getting the table rows")
        rows = []
        for tr in table.locator("tbody tr").all():
            cells = [td.inner_text().strip() for td in tr.locator("td").all()]
            row = {headers[i]: cells[i] for i in range(min(len(headers), len(cells)))}
            rows.append(row)

        logger.info("The data was extracted with success")
        return rows

    def run(self) -> List[Dict]:
        """Execute the scraping workflow and return collected rows."""
        logger.info("Start the Automation")
        self.navigate_to_url()
        self.filter_and_generate_table()
        rows = self.get_table()
        return rows


