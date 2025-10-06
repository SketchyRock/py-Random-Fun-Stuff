"""Program assigns tasks evenly between two people.

Author: Enzo Hins
Version: 9/18/2025
"""


def assign_task(new_task, set1, set2):
    """Assign a new task to one of two sets to keep them balanced.

    Args:
        new_task (str): The task to be assigned.
        set1 (set): First person's set of tasks.
        set2 (set): Second person's set of tasks.

    Returns:
        bool: True if the sets are balanced, False if the task
              was added to balance the sets.
    """
    set3 = set1.union(set2)

    if new_task not in set3:
        if len(set1) == len(set2):
            set1.add(new_task)
        elif len(set1) < len(set2):
            set1.add(new_task)
        else:
            set2.add(new_task)
        
    diff = abs(len(set1) - len(set2))
    
    if diff <= 1:
        return True
    else:
        return False


if __name__ == "__main__":

    my_work = set(["sweep", "windows", "laundry"])
    your_work = set()
    print(assign_task("tidy", my_work, your_work))
    print(my_work, your_work)
    print(assign_task("sweep", my_work, your_work))
    print(my_work, your_work)
    print(assign_task("garbage", my_work, your_work))

