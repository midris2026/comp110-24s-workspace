"""EX01 - Simple Battleship - A cute step towards Battleship."""

__author__ = "730569217"

pick: int = int(input("Pick a secret boat location between 1 and 4: "))
if pick > 4:
    print(f"Error! {pick} too high!")
    exit()
if pick < 1:
    print(f"Error! {pick} too low!")
    exit()

guess: int = int(input("Guess a number between 1 and 4: "))
if guess > 4:
    print(f"Error! {guess} too high!")
    exit()
if guess < 1:
    print(f"Error! {guess} too low!")
    exit()

if guess == pick:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

guess_result: str = ""
if guess == pick:
    guess_result = RED_BOX
else:
    guess_result = WHITE_BOX

if guess == 1:
    print(guess_result + "\U0001F7E6" + "\U0001F7E6" + "\U0001F7E6")
if guess == 2:
    print("\U0001F7E6" + guess_result + "\U0001F7E6" + "\U0001F7E6")
if guess == 3:
    print("\U0001F7E6" + "\U0001F7E6" + guess_result + "\U0001F7E6")
if guess == 4:
    print("\U0001F7E6" + "\U0001F7E6" + "\U0001F7E6" + guess_result)
