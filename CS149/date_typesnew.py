"""Program returns dates in a more verbal format.

Author: Enzo Hins
Version: 9/10/2025
"""


def date_analysis(weekday, month, mo_date):
    """Converts three ints into type of day, season, and portion of the month.

    Args:
        weekday (int): 1–7 inclusive, where 1 is Sunday, 2 is Monday, … 7 is Saturday.
        month (int): 1–12 inclusive, where 1 is January … 12 is December.
        mo_date (int): 1–31 inclusive, representing day of the month.

    Returns:
        tuple: (day_type, season, portion)
    """

    if weekday < 1 or weekday > 7:
        day_type = "invalid"
    else:
        day_type = "weekend"

    if month < 1 or month > 12:
        season = "Invalid"
    elif month in (12, 1, 2):
        season = "Winter"
    elif month in (3, 4, 5):
        season = "Spring"
    elif month in (6, 7, 8):
        season = "Summer"
    else:
        season = "Fall"

    if mo_date < 1:
        quarter = 0
    elif mo_date <= 7:
        quarter = 1
    elif mo_date <= 14:
        quarter = 2
    elif mo_date <= 21:
        quarter = 3
    elif mo_date <= 28:
        quarter = 4
    else:
        quarter = 5

    return (day_type, season, quarter)


if __name__ == "__main__":
    print(date_analysis(6, 8, 18))
    print(date_analysis(0, 1, 26))