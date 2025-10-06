"""Program takes player stats and displays them neatly.

Author: Enzo Hins
Version: 9/18/2025
"""


def player_stats(items):
    """Calculate statistics from a list of player scores.

    Args:
        items (list): List of integers representing player scores.

    Returns:
        dict: Dictionary containing:
            - "total": Sum of all scores.
            - "average": Average of scores.
            - "zeros": Number of games with 0 points.
            - "final": Score of the last game.
    """
    player_dict = {}
    sum_of_items = sum(items)
    length = len(items)

    player_dict.update(total=sum_of_items)
    player_dict.update(average=sum_of_items/length)
    player_dict.update(zeros=items.count(0))
    player_dict.update(final=items[length - 1])

    return player_dict


def print_stats(name, items):
    """Print formatted player statistics.

    Args:
        name (str): Player's name.
        items (list): List of integers representing player scores.
    """
    player_dict = player_stats(items)
    
    print(f"--{name}--")
    print(f"  Total points: {player_dict['total']}")
    print(f"  Average points: {player_dict['average']:.1f}")
    print(f"  Number of 0 point games: {player_dict['zeros']}")
    print(f"  Final game score: {player_dict['final']}")


if __name__ == "__main__":
    
    stats = player_stats([19, 6, 12, 22, 22, 17])
    print(stats)
    print_stats("Kiki Jefferson", [19, 6, 12, 22, 22, 17])