"""Program converts number into phone number format.

Author: Enzo Hins
Version: 9/10/2025
"""


def format(number):
    """Format a phone number for printing.

    Args:
        number (int): 10-digit phone number.

    Returns:
        str: Formatted as "123-456-7890".
    """
    
    first = number // 10000000
    middle = (number // 10000) % 1000
    last = number % 10000

    return f"{first:03d}-{middle:03d}-{last:04d}"


def checksum(number):
    """Get the checksum of a phone number.

    Args:
        number (int): 10-digit phone number.

    Returns:
        int: Sum of the last four digits.
    """
    one = (number // 1000) % 10
    two = (number // 100) % 10
    three = (number // 10) % 10
    four = number % 10

    return one + two + three + four


if __name__ == "__main__":
    print(format(1234567890))
    print(checksum(1234567890))
