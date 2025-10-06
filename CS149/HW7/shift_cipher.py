"""Exercise 7.3 Shift Cipher.

Author: Enzo Hins
Version: 10/3/2025
"""


def encode(text, shift):
    """Encode the given text using the given shift.

    Assume the text is all lowercase and the shift is between +/- 26.
    No error handling.

    Args:
        text (str): the plain text
        shift (int): the shift for the cipher

    Returns:
        str: the encoded text

    >>> encode("the quick brown fox.", 4)
    'xli uymgo fvsar jsb.'
    """
    encoded = ""

    for character in text:
        if ord("a") <= ord(character) <= ord("z"):
            encoded += chr((ord(character) - ord("a") + shift) % 26 + ord("a"))
        else:
            encoded += character

    return encoded


if __name__ == "__main__":
    import doctest
    doctest.testmod()
