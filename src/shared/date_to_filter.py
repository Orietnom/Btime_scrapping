from datetime import datetime, timedelta


def date_to_filter(days_before: int = 0):
    """Return a formatted date string for the given offset.

        Args:
            days_before: Number of days to subtract from the current date.
        """
    formatted_date = datetime.now() - timedelta(days=days_before)
    return formatted_date.strftime("%d/%m/%Y")
