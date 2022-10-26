import turtle
t=turtle.Turtle()

list=['yellow','blue','orange','black','pink','red']
t.speed(0)
for i in range(120):
  t.color(list[i%6])
  t.pensize(i/10+1)
  t.forward(i)
  t.left(59)

