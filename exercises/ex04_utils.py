"""EX04 - Utils."""

__author__ = "730677039"


def all(list: list[int], number: int) -> bool:
    """Figuring out if all the integers are the same."""
    if len(list) == 0:
        return False
    
    i: int = 0
    while i < len(list):
        if list[i] != number:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Return the largest in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list.")
    i: int = 0
    largest_num: int = input[0]
    while i < len(input):
        if input[i] > largest_num:
            largest_num = input[i]
        i += 1
    return largest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """See if lists are equal to each other."""
    i: int = 0

    if len(list1) != len(list2):
        return False
    while i < len(list1) and i < len(list2):
        num1: int = list1[i]
        num2: int = list2[i]
        if num1 == num2:
            i += 1
        else:
            return False
        
    return True


def extend(a: list[int], b: list[int]) -> None:
    """Append to first list."""
    i = len(a)

    for i in range(len(b)):
        a.append(b[i])
    print(a)
    return

