'''
Kevin Joarand
03.02.2022
Ülesanne 04
'''
import itertools

#Tärnid
k = 5
for i in range (1,k+1):
 print(k)
 k = k - 1
gen = itertools.product((0,1),repeat=25)

#Jalgpalli meeskond
sugu = input("Sisesta oma sugu M või N: ")
    if sugu == "M":
    vanus = int(input("Sisesta oma vanus: "))
    if vanus >= 16 and vanus <= 18:
    print ("Sobib meeskonda")
    else:
        print("Ei sobi meeskonda")

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