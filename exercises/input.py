"""EX02 - One Shot Battleship - A cute step towards Battleship."""

__author__ = "730569217"

grid: int = 4
secretr: int = 3
secretc: int = 2 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if rguess == secretr and (cguess == secretc):
    print("Hit!")
elif rguess == secretr and (cguess != secretc):
    print("Close! Correct row, wrong column. ")
else: 
    if cguess == secretc and (rguess != secretr):
        print("Close! Correct column, wrong row. ")
    else:
        print("Miss!")

def input_guess(gridsize: int, row_col: str) -> int:
    """Prompt for and eventually return the user's row or column guess."""
    assert(row_col) == "row" or (row_col) == "column"
    if row_col == "row":
        rguess: int = int(input("Guess a row: "))
        while rguess > grid or rguess < 1:
            rguess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
        return rguess
    if row_col == "column":
        cguess: int = int(input("Guess a column: "))
        while cguess > grid or cguess < 1:
            cguess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
        return cguess

rguess: int = input_guess(grid, "row")
cguess: int = input_guess(grid, "column")

def print_grid(gridsize: int, rowguess: int, columnguess: int, answer: bool) -> None:
    "Print the game board"
    


   
