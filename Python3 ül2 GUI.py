'''
Kevin Joarand
Ülesanne 02 GUI
14.03.2022
'''

import turtle

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanne 02")

angle = 20

for i in range(5):
    k1 = turtle.Turtle()
    k1.rt(angle)
    k1.forward(100)
    angle+=144
    
turtle.exitonclick()