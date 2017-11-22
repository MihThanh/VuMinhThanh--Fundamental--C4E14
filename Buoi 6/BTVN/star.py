from turtle import *
shape('turtle')
def star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        forward(100)
        right(144)

star(-120,-100, 100)
mainloop()
