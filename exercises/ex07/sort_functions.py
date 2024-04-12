"""Functions that implement sorting algorithms."""

__author__ = "730569217"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    index: int = 0

    while index < len(x) - 1:
        us_index: int = index + 1
        element: int = x[us_index]

        while us_index > 0 and element < x[us_index - 1]:
                x[us_index] = x[us_index - 1]
                x[us_index - 1] = element
                us_index -= 1
        index += 1   



def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for counter in range(len(x)):
        min_elem = x[counter]
        me_index = counter
        second_counter = counter + 1

        while second_counter < len(x):
            if x[second_counter] < min_elem:
                min_elem = x[second_counter]
                me_index = second_counter
            second_counter += 1
        
        x[counter], x[me_index] = x[me_index], x[counter]           
    return None
    