"""Program returns dates in a more verbal format.

Author: Enzo Hins
Version: 9/10/2025
"""


def date_analysis(weekday, month, mo_date):
    """Converts three ints into type of day, season, and quarter of the month.

    Args:
        weekday (int): 1–7 inclusive, where 1 is Sunday, 2 is Monday, etc.
        month (int): 1–12 inclusive, where 1 is January, 2 is Februrary, etc.
        mo_date (int): 1–31 inclusive, represents day of month.

    Returns:
        tuple: (day_type, season, quarter)
    """

    if weekday < 1 or weekday > 7:
        day_type = "invalid"
    elif weekday in (1, 7):
        day_type = "weekend"
    else:
        day_type = "weekday"

    if month < 1 or month > 12:
        season = "Invalid"
    elif month <= 2 or month == 12:
        season = "Winter"
    elif month <= 5:
        season = "Spring"
    elif month <= 8:
        season = "Summer"
    else:
        season = "Fall"

    if mo_date < 1:
        quarter = 0
    elif mo_date > 28:
        quarter = 5
    else:
        quarter = (mo_date - 1) // 7 + 1

    return (day_type, season, quarter)


if __name__ == "__main__":
    print(date_analysis(6, 8, 18))
    print(date_analysis(0, 1, 26))
