"""Program converts values of distance and speed.

Author: Enzo Hins
Version: 9/10/2025
"""


def kilometers_to_miles(kilometers):
    """Converts kilometers to miles.

    Args:
        kilometers (float): distance in kilometers.

    Returns:
        float: distance in miles.
    """

    return kilometers / 1.60934


def miles_to_kilometers(miles):
    """Converts miles to kilometers.

    Args:
        miles (float): distance in miles.

    Returns:
        float: distance in miles.
    """

    return miles * 1.60934


def meters_per_second_to_miles_per_hour(meters_per_second):
    """Converts meters per second to miles per hour.

    Args:
        meters_per_second (float): speed in meters per second.

    Returns:
        float: speed in miles per hour.
    """

    return (meters_per_second * (3600 / (1000 * 1.60934)))


def miles_per_hour_to_meters_per_second(miles_per_hour):
    """Converts miles per hour to meters per second.

    Args:
        miles_per_hour (float): speed in miles per hour.

    Returns:
        float: speed in meters per second.
    """

    return (miles_per_hour * ((1000 * 1.60934) / 3600))


if __name__ == "__main__":

    km1 = 4.9
    mi1 = kilometers_to_miles(km1)
    print(f"{km1:.1f} km = {mi1:.1f} mi")

    mi2 = 4.9
    km2 = miles_to_kilometers(mi2)
    print(f"{mi2:.1f} mi = {km2:.1f} km")

    mps1 = 4.9
    mph1 = meters_per_second_to_miles_per_hour(mps1)
    print(f"{mps1:.1f} mps = {mph1:.1f} mph")

    mph2 = 4.9
    mps2 = miles_per_hour_to_meters_per_second(mph2)
    print(f"{mph2:.1f} mph = {mps2:.1f} mps")
