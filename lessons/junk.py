
# hard way to do a square
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
leo.forward(300)
leo.left(90)
done()

# easier way to do a square
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1
done()




leo.begin_fill("blue")
leo.fillcolor(99, 204, 250)
leo.end_fill()
done()


done()