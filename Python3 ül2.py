# Kevin Joarand
# 31.01.2022
# Ülesanne 02
import math



print("Kolmurga ümbermõõt")
#kolmnurga ümbermõõõõõõt
a,b,c = 1,2,3
p= a+b+c
print("Kolmnurga ümbermõõt on:",p)

print("----------------------")
print("Toote hind")
#toote hinna leidmineeeee
hind = 36.75
ale = 0.4
kogus = 3
summa = (hind-(hind*ale))*3
print("Kolme toote summa:",summa, "€")

print("----------------------")
print("Pitsa")
#pitsa eest maksmine
hind = 12.90
jootraha = 0.1
summa = hind * jootraha
print("Igaüks peab maksma:",summa,"€")

print("----------------------")
#keskmine kiirus
kiirus = 29.9
aeg = 24
kaugus = kiirus * aeg
print("24 Min jõuab:",kaugus,)

print("----------------------")
#Leia kolmnurga hüpotenuus
a = 16
b = 9
c = math.sqrt(a**2+b**2)
print("Kolmnurga hüpotenuus on:",c, "cm2")

print("----------------------")
#Ajateisendus
minutid = int(input("Sisesta minutid:"))
sisestus = minutid//60
vastus = minutid % 60
print("Tunde on:",sisestus )

print("----------------------")
#Arvusüsteemid
arv = int(input("Sisesta 10nd arv: "))
print(bin(arv))
print(hex(arv))

#Kütusekulu arvutamine
print("----------------------")
kutus = int(input("Sisesta kütuse liitrid:"))
kilomeetrid = int(input("Sisesta läbitud kilomeetrid:"))
keskmine = 100
kutusekulu = kutus/(kilomeetrid*100)
print(kutusekulu)

