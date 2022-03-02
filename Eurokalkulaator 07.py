'''
Kevin Joarand
Iseseisev töö 07
03.02.2022
'''

# Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.

# Tehakse arvutused sisestatud arvuga.
import math
from tracemalloc import start

def euro(e):
    v = e * 15.65
    return v

def kroon(k):
    v = k / 15.65
    return v

#Antakse valida kas teha EURO->EEK või EEK->EURO ja kuvatakse vastus vastavalt valikule.
print("Vali valuuta \n1 EUR \n2 EEK")
valuuta = int(input("Vali soovitud valuuta number: "))
if valuuta ==1:
    print("----------------------------------\n Valisid EURO")
    a = int(input("Sisesta EURO: "))
    print(euro(a))

elif valuuta ==2:
    print("----------------------------------\n Valisid EEK")
    b = int(input("Sisesta EEK: "))
    print(kroon(b))

# Kuvatakse veateade kui valik on vale
else:
    print("Sellist valikut pole")