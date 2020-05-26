from datetime import datetime


def checkDate(date: str) -> bool:
    """Check valid date string or not"""
    try:
        date = datetime.strptime(date, '%d.%m.%Y')
        return date < datetime.now()
    except:
        return False
