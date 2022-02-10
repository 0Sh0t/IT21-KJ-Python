#Peedu Erik Pajo
#Ülesanne 4
#03.02.2022

#tärn
'''
for i in range(0,5):           
    for j in range(0,5):       
        print('* ', end='')
    print()
       '''          

    
    







#jalgpall

sugu = input("Sisesta sugu: ")
if sugu == "mees":
    vanus = int(input("Sisesta vanus: "))
    if vanus >= 16 and vanus <=18:
         print("Sobid meeskonda")
    
    
#müük

hind = int(input("Sisesta toote hind: "))
if hind <= 10:
    ale = 0.1
else:
    ale = 0.2
tootehind = hind-(hind*ale)

print("Tootehind on:",tootehind)

     
#juubel

aasta = input("Sisesta sünniaeg kujul dd.mm.yyyy:")
d,m,y = aasta.split(".")
aasta1 = 2022
aasta2 = aasta1 - int(y)
if aasta2%5==0:
    print("sul on juubel")
else:
    print("sul pole juubel")


#matemaatika

a = int(input("Siesta arv1: "))
b = int(input("Sisesta arv2: "))
tehe = input("Vali tehe:\n + Liitmine \n - Lahutamine \n * Korrutamine \n / Jagamine \n")


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


#ruut kontroll

a = int(input("sisesta ruudu 1 külg: "))
b = int(input("sisesta ruudu teine külg: "))
if a == b:
    print("Tegemist on ruuduga")
else:
    print("Tegemist on ristkülikuga")