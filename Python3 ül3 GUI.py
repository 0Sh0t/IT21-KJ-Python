'''
Kevin Joarand
Ülesanne 03 GUI
15.03.2022
'''

from tkinter import *

#akna seaded
aken = Tk()
aken.title( "Ülesanne 03")
aken.configure(background='black')
aken.geometry("300x300+100+100")
aken.minsize(200,100)
aken.maxsize(800, 400)

#tekst
tekst = Label(aken, text="Nimi: Kevin Joarand\nRühm: IT21\n 2022", foreground="red", background="black", font="Tahoma 16 bold italic").pack()
tekst.pack()
Label(aken, text="Lorem Ipsum", foreground="red", background="black", font="Tahoma 16 bold italic").pack()

aken.mainloop()

tkinter.exitonclick()