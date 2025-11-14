from datetime import date

def is_valid_date(birthday: date, start: date, end: date) -> bool:
    adjusted_birthday = birthday.replace(year = start.year)
    if adjusted_birthday < start and adjusted_birthday.year != end.year:
        adjusted_birthday = adjusted_birthday.replace(year = end.year)
    if start <= adjusted_birthday <= end:
        return True
    return False
