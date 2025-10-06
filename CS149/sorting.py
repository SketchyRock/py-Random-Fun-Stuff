"""Program swaps items and sorts them from smallest to largest.

Author: Enzo Hins
Version: 9/18/2025
"""


def swap(items, x, y):
    """Swap two elements in a list.

    Args:
        items (list): The list containing elements to be swapped.
        x (int): Index of the first element.
        y (int): Index of the second element.
    """
    temp = items[x]
    items[x] = items[y]
    items[y] = temp


def sort_short(items):
    """Sort a list of up to three items in ascending order.

    Args:
        items (list): The list of integers (length 0–3) to be sorted.
    """
    length = len(items)
    
    if length < 2:
        return

    if items[0] > items[1]:
        swap(items, 0, 1)

    if length == 3:
        
        if items[1] > items[2]:
            swap(items, 1, 2)
            
            if items[0] > items[1]:
                swap(items, 0, 1)


if __name__ == "__main__":

    items = [1]
    sort_short(items)
    assert items == [1]

    items = [2, 1]
    sort_short(items)
    assert items == [1, 2]

    items = [3, 2, 1]
    sort_short(items)
    assert items == [1, 2, 3] 
