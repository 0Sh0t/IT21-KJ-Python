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
     
#Arvamine
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


#Kolmnurk
for i in range (1,11):
    print("*"* i)

k=5
for i in range (1,6):
    print("*"* k)
    k -= 1


#
for i in range (1,11):
    print("*"* i)

for a in range(1.10):
    if a%2==0:
        print(f"{a} paaris")
    else:
        print(f"{a} paaritu")

for b in range (1.10)
    print


import itertools

#Tärnid
import random

arv = random.randint(1.10)

print(random.randrange(1.10)


gen = itertools.product((0,1),repeat=25))
k = 5
for i in range (1,k+1):
 print(k)
 k = k - 1

#Jalgpalli meeskond
sugu = input("Sisesta oma sugu M või N: ")
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