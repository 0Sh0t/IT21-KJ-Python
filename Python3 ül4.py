'''
Kevin Joarand
03.02.2022
Ülesanne 04
'''

#Ruutude ja kuupide tabel










#Pank
konto = 0
raha = int(input("Pane raha panka: "))
intress = 0.05
aastad = 5
konto += raha
print(f"{'Aasta':10} {'Algsumma':10} {'Intress':10} {'Aasta lõpuks':10}")


for r in range(aastad):
     kasum = konto*intress
     print(f"{r:5} {konto:10.2f} {kasum:10.2f} {konto+kasum:10.2f}")
     konto+=kasum
     
#Arvamismäng
'''
import random

loop = 1
korrad = 1
suv = random.randint(1,10)

while loop==1:
    if korrad <= 3:
        arv = int(input("Arva ära arv 1-10: "))
    else:
        veel = int(input("Tahad veel mängida? jah/ei: "))
            if veel=="jah":
        korrad = 0
    else:
        loop = 0
    
    korrad += 1

    if arv == suv:
        print("Arvasid ära")
        loop = 0
    else:
        print("Ei arvanud ära")
print(suv , arv)
'''

#Pisike korrutustabel
for k in range(1,11):
    arv = 5
    v = k * arv
    print(f"{arv} x {k} = {v}")

#Paaris ja paaritu

for c in range(1, 100):
    if c==5:
        break
    print(c, end='')

#Loto

import random
print(random.randrange(0,99999))

#Kolmnurk
for i in range (1,11):
    print("*"* i)

k=5
for i in range (1,6):
    print("*"* k)
    k -= 1


'''
for i in range (1,11):
    print("*"* i)

for a in range(1.10):
    if a%2==0:
        print(f"{a} paaris")
    else:
        print(f"{a} paaritu")

for b in range (1.10)
    print

'''
import itertools


#Tärnid
k = 5
for i in range(1,6):
        print("*    "* k)
        k += 1
for a in range(1,6):          
    for b in range(1,6):       
        print("*    ", end='')
    print()
k = 5
for i in range(1,6):
        print("*    "* k)
        k -= 1


#Jalgpalli meeskond


sugu = input("Sisestage oma sugu M/N: ")
if sugu == "M":
    vanus = int(input("Sisestage oma vanus: "))
    if vanus >= 16 and vanus <= 18:
        print("Sobib meeskonda")
else :
    print("Ei sobi meeskonda")
'''
sugu = input("Sisesta oma sugu M/N: ")
    if sugu == "M":
        vanus = int(input("Sisesta oma vanus: "))
    
    if vanus >= 16 and vanus <= 18:
    print ("Sobib meeskonda")
    else:
        print("Ei sobi meeskonda")
'''
#Müük
a = int(input("Sisesta toote hind: "))
if a <=10:
    allahindlus = 0.1
else:
    allahindlus = 0.2
hind = a - a*allahindlus
print("hind on:", hind)


#Juubel
aasta = input("sisesta sünniaeg kujul dd.mm.yyyy:")
d,m,y = aasta.split(".")
aasta1 = 2022
aasta2 = aasta1 - int(y)
if aasta2%5==0:
    print("sul on juubel")
else:
    print("sul pole juubel")

#Matemaatika

a = int(input("Siesta arv1: "))
b = int(input("Sisesta arv2: "))
tehe = input("Vali tehe:\n + Liitmine \n - Lahutamine \n * Korrutamine \n : Jagamine \n")


if tehe=="+":
    v = a + b
elif tehe=="-":
    v = a - b
elif tehe=="*":
    v = a * b
elif tehe==":":
    v = a / b

else:
    vastus
print(f"{a}{tehe}{b}={v}")

#Ruut
B = int(input("1. külg: "))
D = int(input("2. külg: "))

if B==D:
        print("Ruut")
else:
        print("Ristküik")