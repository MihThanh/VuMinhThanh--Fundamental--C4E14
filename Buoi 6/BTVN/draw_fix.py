from turtle import *
shape('turtle')
speed(0)
def draw_square(length, color_sign):
    for i in range(4):
        color(color_sign)
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
