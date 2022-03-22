'''
Kevin Joarand
Ülesanne 05 GUI
22.03.2022
'''

from tkinter import *

#Akna seaded
aken = Tk()
aken.title('Käibemaksukalkulatoor')
aken.geometry("300x200")


def summa():
    global protsent
    global a
    a = int(sisestus.get())
    protsent = int(var.get())
    kaibemaks = (a/100*protsent)
    hind = (a+kaibemaks)
    valjund2.config(text=f"{kaibemaks}€")
    valjund3.config(text=f"{hind}€")
    
    
#Kuva
kaibemaksuta = Label(aken, text="Hind käibemaksuta:")
kaibemaksuta.grid(row=0,column=0)
valjund = Label(aken, text="------------------------------------------------------------------")
valjund.grid(row=6,columnspan=3)
valjund = Label(aken, text="Käibemaksu määr:")
valjund.grid(row=4,column=0)
valjund = Label(aken, text="Käibemaks:")
valjund.grid(row=7,column=0)
valjund2 = Label(aken, text="")
valjund2.grid(row=7,column=1)
valjund = Label(aken, text="Hind käibemaksuga:")
valjund.grid(row=8,column=0)
valjund3 = Label(aken, text="")
valjund3.grid(row=8,column=1)

#Kasutaja sisestus
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)

nupp1 = Button(aken, text="OK", width=10, command=summa)
nupp1.grid(row=9, column=1)

#Antakse valik 9% ja 20% vahel
var = IntVar()
valik = Radiobutton(aken,text="9%", variable=var, value=9)
valik.grid(row=4, column=1)
valik = Radiobutton(aken,text="20%", variable=var, value=20)
valik.grid(row=5, column=1)

aken.mainloop()