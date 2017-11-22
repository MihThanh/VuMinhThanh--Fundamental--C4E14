from turtle import *
shape('turtle')
def draws(length, color_sign):
    for i in range(4):
        color(color_sign)
        forward(length)
        left(90)
draws(100, 'blue')
mainloop()
