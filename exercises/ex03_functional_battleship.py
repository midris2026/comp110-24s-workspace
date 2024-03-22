"""EX03 - Functional Battleship."""

__author__ = "730569217"

import random

grid: int = 4
secretr: int = 3
secretc: int = 2 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
 

def input_guess(gridsize: int, row_col: str) -> int:
    """Prompt for and eventually return the user's row or column guess."""
    assert (row_col) == "row" or (row_col) == "column"
    guess: int = 0
    if row_col == "row":
        guess = int(input("Guess a row: "))
        while guess > gridsize or guess < 1:
            guess = int(input(f"The grid is only {gridsize} by {gridsize}. Try again: "))

    if row_col == "column":
        guess = int(input("Guess a column: "))
        while guess > gridsize or guess < 1:
            guess = int(input(f"The grid is only {gridsize} by {gridsize}. Try again: "))
    return guess
        

def print_grid(gridsize: int, rowguess: int, columnguess: int, answer: bool) -> None:
    """Print the game board."""  
    guess_result: str = ""
    if answer:
        guess_result = RED_BOX
    else:
        guess_result = WHITE_BOX
    rcounter: int = 1
    while rcounter <= gridsize:
        row: str = ""
        ccounter: int = 1
        if rowguess == rcounter: 
            while ccounter <= gridsize:
                if ccounter == columnguess:
                    row += guess_result
                    ccounter += 1
                else: 
                    row += BLUE_BOX
                    ccounter += 1
        else:
            while ccounter <= gridsize:
                row += BLUE_BOX
                ccounter += 1
        rcounter += 1 
        print(row)


def correct_guess(secretrow: int, secretcolumn: int, rowguess: int, columnguess: int) -> bool:
    """Whether user is correct or not."""
    if rowguess == secretrow and columnguess == secretcolumn:
        return True
    else:
        return False
    

def main(gridsize: int, secretrow: int, secretcolumn: int) -> None:
    """Pull everything together."""
    current_turn: int = 1
    last_turn: int = 5
    while current_turn <= last_turn:
        print(f"=== Turn {current_turn}/{last_turn} ===")
        row: int = input_guess(gridsize, "row")
        column: int = input_guess(gridsize, "column")
        match: bool = correct_guess(secretrow, secretcolumn, row, column)
        print_grid(gridsize, row, column, match)
        if match:
            print("Hit!")
            print(f"You won in {current_turn}/{last_turn} turns!")
            return
        else:
            print("Miss!")
            current_turn += 1
    print(f"X/{last_turn} - Better luck next time!")
    return


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
