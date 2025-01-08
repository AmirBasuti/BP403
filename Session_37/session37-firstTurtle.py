from turtle import *
color('red', 'yellow')
# begin_fill()

myScr = Screen()
while True:
    forward(200)
    right(110)
    if abs(pos()) < 1:
        break
# end_fill()
done()

myScr.exitonclick()