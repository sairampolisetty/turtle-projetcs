import turtle

t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("green")
t.pensize(2)
t.speed(0)
t.begin_fill()
t.fillcolor('red')
for i in range(4):
    t.fd(100)
    t.rt(90)

t.end_fill()
t.hideturtle()
