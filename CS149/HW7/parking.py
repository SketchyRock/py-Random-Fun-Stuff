"""Exercise 7.4 Parking Lot.

Author: Enzo Hins
Version: 10/3/2025
"""


def best_fit(car, spots):
    """Return the best fitting parking spot for the car.

    Select the smallest legal spot. There must be at least two feet
    of space around all sides of the car when parked. In the case of
    ties, the spot with the larger index should be selected.

    Args:
        car (tuple): Dimensions of the car to park
        spots (list of tuples): The spots available

    Returns:
        int or None: the index of the best fitting spot

    >>> best_fit((3, 4), [(5, 5), (10, 12), (7, 8), (7, 9), (8, 8)])
    2
    >>> best_fit((3, 4), [(5, 5), (10, 12), (3, 4), (7, 9), (8, 8)])
    3
    >>> best_fit((3, 4), [(5, 5), (10, 12), (3, 4), (7, 9), (7, 9)])
    4
    >>> best_fit((9, 12), [(5, 5), (10, 12), (3, 4), (7, 9), (7, 9)])
    """
    
    index = None
    min_area = None
    required_width = car[0] + 4
    required_length = car[1] + 4

    for i, spot in enumerate(spots):
        spot_width = spot[0]
        spot_length = spot[1]
        
        if spot_width >= required_width and spot_length >= required_length:
            area = spot_width * spot_length
            
            if (min_area is None or area < min_area or (area == min_area and i > index)):
                min_area = area
                index = i

    return index


if __name__ == "__main__":
    import doctest
    doctest.testmod()
