"""HW6.3 Wheel of Fortunate Events.

Author: Enzo Hins
Version: 9/29/2025
"""

import random


def spin_wheel():
    """Spin the wheel and return the result of the spin.

    Returns:
        int: the amount of money won, or 0 if game over

    >>> random.seed(0)
    >>> spin_wheel()
    0
    >>> spin_wheel()
    100
    >>> spin_wheel()
    20
    """
    
    spin = random.random()

    if spin < 0.25:
        return 1
    elif spin < 0.5:
        return 20
    elif spin < 0.65:
        return 50
    elif spin < 0.775:
        return 100
    elif spin < 0.80:
        return 1000
    else:
        return 0


def play_game():
    """Simulate playing the game until a game over.

    Returns:
        int, int: total cash won and total number of spins

    >>> random.seed(0)
    >>> play_game()
    (0, 1)
    >>> play_game()
    (1300, 10)
    >>> play_game()
    (240, 6)
    """

    cash = 0
    spins = 0
    
    while True:
        wheel_spin = spin_wheel()
        spins += 1
        
        if wheel_spin == 0:
            break
        
        cash += wheel_spin
    
    return (cash, spins)
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()
