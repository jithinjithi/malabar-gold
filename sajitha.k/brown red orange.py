from turtle import*
clear()
pensize(3)
clr=["blue","brown","green","purple","red","ornge"]
for i in clr:
    right(60)
    color("black",i)
    begin_fill()
    for j in range(4):
      forward(100)
      rt(90)
    end_fill()
input()