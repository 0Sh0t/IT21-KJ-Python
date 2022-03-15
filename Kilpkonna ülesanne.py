'''
Kevin Joarand
Kilpkonn
14.03.2022
'''

import turtle

#Akna seaded
aken = turtle.Screen()
aken.setup(500,500)
aken.title("Ülesanne")
nurk = 0
#Funktsioon ruudu tekitamiseks
for i in range(2):
    t=turtle.Turtle()
    t.right(nurk)
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    nurk = 45
    

turtle.exitonclick()