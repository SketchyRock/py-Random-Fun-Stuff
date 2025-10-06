"""HW6.2 Dice Rolling Simulator.

Author: Enzo Hins
Version: 9/29/2025
"""

import random


def roll_dice(num_dice, num_sides):
    """Roll a number of dice and return the sum.

    Args:
        num_dice (int): the number of dice to roll
        num_sides (int): the number of sides on each die

    Returns:
        int: the sum of all the faces of the rolled dice

    >>> random.seed(0)
    >>> roll_dice(0, 1)
    -1
    >>> roll_dice(1, 6)
    4
    >>> roll_dice(3, 20)
    25
    """
    
    if num_dice <= 0 or num_sides <= 0:
        return -1
    
    i = 0
    total = 0
    
    while i < num_dice:
        total += random.randint(1, num_sides)
        i += 1
        
    return total


if __name__ == "__main__":
    import doctest
    doctest.testmod()
