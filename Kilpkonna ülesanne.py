'''
Kevin Joarand
Kilpkonn
14.03.2022
'''

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(500,500)
aken.title("Ülesanne")

angle = 5

#funktsioon ruudu tekitamiseks
def joonista_ruut(pikkus):
    t = turtle.Turtle()
    for x in range(0,2):
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        #t.rt(angle)

joonista_ruut(50)

turtle.exitonclick()