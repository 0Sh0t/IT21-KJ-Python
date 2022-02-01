'''
Kevin Joarand
Ülesanne 03
01.02.2022
'''

#Palindroom
palindroom = input("Sisesta palindroom: ")
print(palindroom == palindroom[::-1])

#Tundide ajad
algus = input("Algusaeg: ")
lõpp = input("Lõppaeg: ")
hh1, mm1 = algus.split(":")
hh2, mm2 = lõpp.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1))
h = vastus//60
v = vastus % 60
print(f"Õpilase päeva pikkus on {h}:{v}")

#Email
email = input("Sisesta oma email: ")
print("@" in email)

#Vandumine
s = input("Ära kurat ütle: ")
s = s.lower()
v = s.replace("kurat","***")
print(v)

#Korralik nimi
nimi = input("Sisesta nimi: ")
nimi = nimi.strip().capitalize()
print("Tere",nimi)