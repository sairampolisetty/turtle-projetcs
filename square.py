import turtle

t = turtle.Turtle()
t.pensize(3)
t.begin_fill()
t.fillcolor('red')
for i in range(4):
    t.fd(100)
    t.rt(90)

t.end_fill()
