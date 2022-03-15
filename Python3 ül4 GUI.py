'''
Kevin Joarand
Ülesanne 04 GUI
15.03.2022
'''
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Kalkulaator')
aken.geometry("200x200")
vastus = Label(aken, text="Siia kunagi vastus!")
vastus.grid(row=0,column=1,columnspan=4,ipadx=45)


#nupud
num7 = Button(aken, text="7", padx=2, pady=2, width=4, font="Tahoma 12")
num7.grid(row=1, column=1, pady=2, padx=2)
num8 = Button(aken, text="8", padx=2, pady=2, width=4, font="Tahoma 12")
num8.grid(row=1, column=2, pady=2, padx=2)
num9 = Button(aken, text="9", padx=2, pady=2, width=4, font="Tahoma 12")
num9.grid(row=1, column=3, pady=2, padx=2)
jagamine = Button(aken, text="/", padx=2, pady=2, width=4, font="Tahoma 12")
jagamine.grid(row=1, column=4, pady=2, padx=2)
num4 = Button(aken, text="4", padx=2, pady=2, width=4, font="Tahoma 12")
num4.grid(row=2, column=1, pady=2, padx=2)
num5 = Button(aken, text="5", padx=2, pady=2, width=4, font="Tahoma 12")
num5.grid(row=2, column=2, pady=2, padx=2)
num6 = Button(aken, text="6", padx=2, pady=2, width=4, font="Tahoma 12")
num6.grid(row=2, column=3, pady=2, padx=2)
korrutamine = Button(aken, text="*", padx=2, pady=2, width=4, font="Tahoma 12")
korrutamine.grid(row=2, column=4, pady=2, padx=2)
num3 = Button(aken, text="3", padx=2, pady=2, width=4, font="Tahoma 12")
num3.grid(row=3, column=1, pady=2, padx=2)
num2 = Button(aken, text="2", padx=2, pady=2, width=4, font="Tahoma 12")
num2.grid(row=3, column=2, pady=2, padx=2)
num1 = Button(aken, text="1", padx=2, pady=2, width=4, font="Tahoma 12")
num1.grid(row=3, column=3, pady=2, padx=2)
lahutamine = Button(aken, text="-", padx=2, pady=2, width=4, font="Tahoma 12")
lahutamine.grid(row=3, column=4, pady=2, padx=2)
num0 = Button(aken, text="0", padx=2, pady=2, width=4, font="Tahoma 12")
num0.grid(row=4, column=1, pady=2, padx=2)
koma = Button(aken, text=",", padx=2, pady=2, width=4, font="Tahoma 12")
koma.grid(row=4, column=2, pady=2, padx=2)
vordub = Button(aken, text="=", padx=2, pady=2, width=4, font="Tahoma 12")
vordub.grid(row=4, column=3, pady=2, padx=2)
liitmine = Button(aken, text="+", padx=2, pady=2, width=4, font="Tahoma 12")
liitmine.grid(row=4, column=4, pady=2, padx=2)


aken.mainloop()