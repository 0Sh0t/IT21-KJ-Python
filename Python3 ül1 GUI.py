'''
Kevin Joarand
Ülesanne 01 GUI
14.03.2022
'''

import turtle
import random

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanne 01")

colors = ('red','blue','green','orange')
spikes = 8
turn = 8
size = 100


for i in range(spikes):
    k1 = turtle.Turtle()
    k1.color(random.choice(colors))
    k1.left(turn)
    k1.forward(size)
    turn+=360/spikes
    
turtle.exitonclick()