from turtle import*
screensize(20, 20)
shape('turtle')
k = 20
speed(10)
penup()
left(180)
forward(10*k)
right(90)
forward(10*k)
right(90)
pendown()
for i in range(2):
    forward(5*k)
    right(90)
    forward(15*k)
    right(90)
penup()
forward(-7*k)
right(90)
forward(12*k)
left(90)
pendown()
for i in range(2):
    forward(65*k)
    right(90)
    forward(120*k)
    right(90)
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x*k, y*k)
        dot(3, 'red')
done()
