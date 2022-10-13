from turtle import*
clear()
pensize(3)
for i in range(6):
    right(60)
    color("black","blue")
    begin_fill()
    for j in range(4):
        forward(100)
        rt(90)
    end_fill()
input()