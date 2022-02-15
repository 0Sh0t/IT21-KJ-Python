'''
Kevin Joarand
Ülesanne 07
15.02.2022
'''

#Ruumalade leidmise programm
import math

def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v

def koonus(k,s):
    v = round(1/3*math.pi*k**2*s,2)
    return v

def silinder(i,e):
    v = round(math.pi*i**2*e,2)
    return v

print("********** LEIAME RUUMALA **********")
print("Vali kujund \n1 Kuup \n2 Kera \n3 Koonus \n4 Silinder \n5 EXIT")
valik = int(input("Vali soovitud kujundi number "))
if valik ==1:
    print("----------------------------------\n Valisid KUUBI ruumala arvutamise")
    a = int(input("Sisesta kuubi külje pikkus a="))
    print(kuup(a))

if valik ==2:
    print("----------------------------------\n Valisid KERA ruumala arvutamise")
    r = int(input("Sisesta kera külje pikkus r="))
    print(kera(r))
    
if valik ==3:
    print("----------------------------------\n Valisid KOONUSE ruumala arvutamise")
    k = int(input("Sisesta koonuse külje pikkus a="))
    s = int(input("Sisesta koonuse külje pikkus b="))
    print(koonus(k,s))

if valik ==4:
    print("----------------------------------\n Valisid SILINDER ruumala arvutamise")
    i = int(input("Sisesta silindri külje pikkus a= "))
    e = int(input("Sisesta silindri külje pikkus b= "))
    print(silinder(i,e))

#Funktsioon tervitab kasutajat, kas eesti, inglise või saksa keeles
def tervita(nimi, keel="de"):
    if keel=="et":
        print (f"Tere {nimi}!")
    elif keel=="en":
        print (f"Hi {nimi}!")
    else:
        print (f"Hallo {nimi}!")
n = input("Sisesta nimi: ")
k = input("Vali keel et/en/de: ")
tervita(n,k)