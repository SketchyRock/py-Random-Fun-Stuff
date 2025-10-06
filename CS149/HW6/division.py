"""HW6.1 Division Algorithm.

Author: Enzo Hins
Version: 9/29/2025
"""


def divide(number, divisor):
    """Divide number by divisor using the integer division algorithm.

    Args:
        number (int): the number to divide
        divisor (int): the number to divide by

    Returns:
        int, int: the quotient and the remainder

    >>> divide(50, 10)
    (5, 0)
    >>> divide(145, 6)
    (24, 1)
    """
    
    q = 0
    r = number
    
    while r >= divisor:
        q += 1
        r -= divisor
    return (q, r)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
