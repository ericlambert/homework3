import turtle
pen = turtle.Pen()
distance = 50
width = 3

pen.penup()
pen.speed(3)

heading = 180
pen.setheading(heading)
pen.forward(distance * 2)

pen.color('red')
pen.width(width)
pen.pendown()

heading -= 45
pen.setheading(heading)
pen.forward(distance)

heading -= 90
pen.setheading(heading)
pen.forward(distance * 2)

heading -= 90
pen.setheading(heading)
pen.forward(distance)

pen.color('blue')

heading += 90
pen.setheading(heading)
pen.forward(distance)

heading -= 90
pen.setheading(heading)
pen.forward(distance * 2)

heading -= 90
pen.setheading(heading)
pen.forward(distance)

pen.penup()
pen.hideturtle()
turtle.done()