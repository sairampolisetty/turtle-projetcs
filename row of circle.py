import turtle

t=turtle.Turtle()
t.up()

def circle(x,color):
    t.goto(x,0)
    t.goto(x,-25)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(30)
    t.end_fill()
    t.up()
    t.home()
circle(0,'yellow')
circle(50,'green')
circle(100,'pink')
circle(150,'blue')