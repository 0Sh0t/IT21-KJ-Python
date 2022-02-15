'''
Kevin Joarand
10.02.2022
Ülesanne 05
'''

#Tärnid

import random
arvud = []
for i in range(6):
    arvud.append(random.randint(1,20))
for n in range(len(arvud)):
    print("*"*arvud[n])

#Vanused

import random

arvud = []
for i in range(5):
    arvud.append(random.randint(1,99))
print(f"suurim arv: {max(arvud)}\n väiksem arv: {min(arvud)}\n summa: {sum(arvud)/len(arvud)} ")    
#for i in range(len(arvud)):
#    print(arvud)

#Duplikaadid

kordused = ['Juhan','Kati','Mario','Mario','Mati','Mati']
puhastatud = []

for i in range(len(kordused)):
    if kordused[i] not in puhastatud:
        puhastatud.append(kordused[i])

for i in range(len(puhastatud)):
    print(puhastatud[i],end=", ")

#Õpilased

opilased = ['Juhan','Kati','Maarja','Mario','Mati']
for i in range(len(opilased)):
    print (f"{i+1}. {opilased[i]}")
valik = int(input("Sisesta number: "))
del opilased[valik-1]

uus_nimi = input("Sisesta uus või muudetud nimi: ")
opilased.insert(valik-1,uus_nimi)

print("Nimi muudetud")
print(opilased)

#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
    