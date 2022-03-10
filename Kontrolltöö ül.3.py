#Kevin Joarand
#Kontrolltöö ül.3
#03.11.2022

import random

a = 0
b = 0


valik=['+','-']

print('Liitmise ja lahutamise õppimine')

while a <10:
    arv1=random.randint(0, 10)
    arv2=random.randint(0, 10)
    tehe=random.choice(valik)

    k=print(arv1, tehe, arv2, '=')

    choice = input(">")


    if tehe== '+':
                    arv=arv1+arv2
                    if int (choice) == arv1+arv2:
                        print ('Õige')
                        b= b+1
                    else:
                        print ('Väär')
    elif tehe== '-':
                    arv=a-b
                    if int (choice) == arv1-arv2:
                        print ('Õige')
                        b= b+1
                    else:
                        print ('Väär')

    a += 1

print ("Tehted said otsa")

arv = 10
print("Sa said %d õiget %d-st" % (b, arv))