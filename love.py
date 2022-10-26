import turtle

t=turtle.Turtle()
wn=turtle.Screen()

wn.bgcolor("black")
t.goto(0,-90)
t.speed(0)
t.color("violet")
t.begin_fill()
t.fillcolor('violet')
t.lt(140)
t.fd(140)
t.circle(-70,200)
t.setheading(60)
t.circle(-70,200)
t.forward(140)
t.end_fill()
t.hideturtle()