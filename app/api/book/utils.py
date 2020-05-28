from datetime import datetime


def checkYearOfPublication(yearOfPublication: str) -> bool:
    """Check valid or not year of publication"""
    try:
        return int(yearOfPublication) <= datetime.now().year
    except:
        return False
