'''
Kevin Joarand
Kontrolltöö ül.3
15.03.2022
'''

import random
game = 1
while game == 1:
    oiged = 0
    korrad = int(input("Sisesta kordade arv"))
    
#Valitakse suvalised arvud
    for i in range(korrad):
        arv1 = random.randint(1, 10)
        arv2 = random.randint(1, 10)
#Tehakse liitmis ja lahutamis tehted
        tehe = random.randint(1, 2)
        if tehe == 1:
            loop = 1
            while loop == 1:
                vastus = arv1 + arv2
                v = int(input(f"{arv1} + {arv2}="))
                if v == vastus:
                    print("Õige")
                    oiged += 1
                    loop = 0
                else:
                    print("Vale")
                
        else:
            loop = 1
            while loop == 1:
                vastus = arv1 - arv2
                v = int(input(f"{arv1} - {arv2}="))
                if v == vastus:
                    print("Õige")
                    oiged += 1
                    loop = 0
                else:
                    print("Vale")

#Kuvab õigete vastuste protsendi ning ütleb kas on vaja veel harjutada
    protsent = oiged / korrad * 100
    print(protsent)
    if protsent > 61:
        print("Tubli")
    else:
        print("Õpi veel")
#Annab valida kas alustada algusest
    kysimus = input("Tahad veel mängida? j või e: " )
    if kysimus =="e":
        game = 0
print("Mäng läbi")