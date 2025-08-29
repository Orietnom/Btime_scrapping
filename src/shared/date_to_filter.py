from datetime import datetime, timedelta


def date_to_filter(days_before: int = 0):
    formatted_date = datetime.now() - timedelta(days=days_before)
    return formatted_date.strftime("%d/%m/%Y")
