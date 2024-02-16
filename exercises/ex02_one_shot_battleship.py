"""EX02 - One Shot Battleship - A cute step towards Battleship."""

__author__ = "730569217"

grid: int = 4
secretr: int = 3
secretc: int = 2 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

rguess: int = int(input("Guess a row: "))
while rguess > grid or rguess < 1:
    rguess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
cguess: int = int(input("Guess a column: "))
while cguess > grid or cguess < 1:
    cguess = int(input(f"The grid is only {grid} by {grid}. Try again: "))


guess_result: str = ""
if rguess == secretr and (cguess == secretc):
    guess_result = RED_BOX
else:
    guess_result = WHITE_BOX

rcounter: int = 1

while rcounter <= grid:
    row: str = ""
    ccounter: int = 1
    if rguess == rcounter: 
        while ccounter <= grid:
            if ccounter == cguess:
                row += guess_result
                ccounter += 1
            else: 
                row += BLUE_BOX
                ccounter += 1
    else:
        while ccounter <= grid:
            row += BLUE_BOX
            ccounter += 1
    rcounter += 1 
    print(row)

if rguess == secretr and (cguess == secretc):
    print("Hit!")
elif rguess == secretr and (cguess != secretc):
    print("Close! Correct row, wrong column. ")
else: 
    if cguess == secretc and (rguess != secretr):
        print("Close! Correct column, wrong row. ")
    else:
        print("Miss!")