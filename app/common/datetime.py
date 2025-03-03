from datetime import timezone, datetime


def get_current_date():
    return datetime.now(timezone.utc)
