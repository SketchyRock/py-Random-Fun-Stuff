"""Program adds specified brightness to rgb colors.

Author: Enzo Hins
Version: 9/18/2025
"""


def adjust_channel(tup, channel, increase):
    """Adjust a single RGB channel by a specified amount, between 0 and 255.

    Args:
        tup (tuple): Original RGB color.
        channel (int): Index of the channel to adjust.
        increase (int): Amount to add (can be negative).

    Returns:
        tuple: New RGB color after adjustment.
    """
    
    value = tup[channel] + increase
    
    if value > 255:
        value = 255
        
    elif value < 0:
        value = 0

    if channel == 0:
        return (value, tup[1], tup[2])
    
    elif channel == 1:
        return (tup[0], value, tup[2])
    
    else:
        return (tup[0], tup[1], value)


def adjust_brightness(tup, increase):
    """Adjust the brightness of all RGB channels by a specified amount.

    Args:
        tup (tuple): Original RGB color.
        increase (int): Amount to add to each channel (can be negative).

    Returns:
        tuple: New RGB color after adjustment.
    """
    new_tup = adjust_channel(tup, 0, increase)
    new_tup = adjust_channel(new_tup, 1, increase)
    new_tup = adjust_channel(new_tup, 2, increase)
    return new_tup


def same_color(tup1, tup2, difference):
    """Check if two RGB colors are within a certain difference per channel.

    Args:
        tup1 (tuple): First RGB color.
        tup2 (tuple): Second RGB color.
        difference (int): Maximum allowed difference per channel.

    Returns:
        bool: True if colors are considered the same, False otherwise.
    """
    if abs(tup1[0] - tup2[0]) > difference:
        return False
    elif abs(tup1[1] - tup2[1]) > difference:
        return False
    elif abs(tup1[2] - tup2[2]) > difference:
        return False
    else:
        return True


if __name__ == "__main__":
    print(adjust_brightness((0, 0, 250), 10))
    print(adjust_brightness((100, 5, 255), -10))
    print(same_color((128, 25, 80), (128, 25, 80), 0))
    print(same_color((129, 25, 80), (128, 25, 80), 0))
    print(same_color((129, 25, 80), (128, 25, 80), 1))
    
