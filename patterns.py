import turtle

t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('yellow')

def circle(x,y,color):
  t.goto(x,y)
  t.down()
  t.begin_fill()
  t.fillcolor(color)
  t.circle(30)
  t.end_fill()
  t.up()
  t.home()
  
circle(0,0,"red")  
circle(100,100,"blue")
circle(0,100,'black')
circle(-100,100,"orange")
circle(0,-100,'black')
circle(-100,-100,"violet")
circle(100,0,'black')
circle(100,-100,"green")
circle(-100,0,'black')