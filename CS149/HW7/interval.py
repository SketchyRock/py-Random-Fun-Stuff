"""Exercise 7.2 Intervals.

Author: Enzo Hins
Version: 10/3/2025
"""


def in_interval(nums, lower, upper, closed=True):
    """Return the numbers in the interval.

    Args:
        nums (list): Original list of float numbers
        lower (float): The lower bound of the interval
        upper (float): The upper bound of the interval
        closed (bool): Whether the bounds are inclusive

    Returns:
        list: the numbers in the interval

    >>> nums = [20.1, 0.0, 2.5, 1.4, -6.0]
    >>> in_interval(nums, 0.0, 5.0)
    [0.0, 2.5, 1.4]
    >>> in_interval(nums, 0.0, 5.0, False)
    [2.5, 1.4]
    """
    num_interval = []

    if closed:
        for num in nums:
            if lower <= num <= upper:
                num_interval.append(num)
    else:
        for num in nums:
            if lower < num < upper:
                num_interval.append(num)

    return num_interval


if __name__ == "__main__":
    import doctest
    doctest.testmod()
