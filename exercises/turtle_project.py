"""Drawing of a starry night above a pyramid."""

__author__ = "730569217"

from turtle import Turtle, colormode, done
colormode(255)
pointer: Turtle = Turtle()


def main() -> None:
    """Entrypoint of my scene."""
    pointer.screen.bgcolor(4, 0, 60)
    stars(pointer, 630, 145)
    trail(pointer, 630, 145, 25)
    trail(pointer, 630, 143, 21)
    stars(pointer, -500, 10)
    stars(pointer, -90, 145)
    stars(pointer, 130, 295)
    moon(pointer, -599, 140)
    pyramid(pointer, 10, -400)


def stars(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a star."""
    a_turtle.penup()
    a_turtle.speed(0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("yellow", "yellow")
    a_turtle.setheading(0.0)
    i: int = 5
    a_turtle.begin_fill()
    while i > 0:
        a_turtle.forward(5)
        a_turtle.right(145)
        i = i - 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def trail(a_turtle: Turtle, x: float, y: float, length: int) -> None:
    """Draws the shooting part of a shooting star."""
    if length < 20:
        return
    else:
        a_turtle.penup()
        a_turtle.speed(0)
        a_turtle.goto(x, y)
        a_turtle.pendown()
        a_turtle.color("yellow")
        a_turtle.backward(length)
        trail(a_turtle, x + length, y, length - 10)
    a_turtle.hideturtle()
    

def moon(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a moon."""
    a_turtle.penup()
    a_turtle.speed(0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.color("grey", "grey")
    a_turtle.begin_fill()
    a_turtle.circle(120)
    a_turtle.end_fill()
    a_turtle.hideturtle()


def pyramid(a_turtle: Turtle, x: float, y: float) -> None:
    """Draw a pyramid."""
    a_turtle.penup()
    a_turtle.speed(0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.color(225, 178, 97)
    i: int = 0
    for i in range(3):
        a_turtle.forward(300)
        a_turtle.left(120)
    a_turtle.end_fill()
    a_turtle.hideturtle()


if __name__ == "__main__":
    main()
    done()