'''
Kevin Joarand
Ülesanne 09
03.03.2022
'''

import datetime

# Eralda iskukoodist sünnikuupäev ja leia isiku vanus
isikukood = input("Sisesta isikukood: ")
aasta = int("20"+isikukood[1] + isikukood[2])
kuu = int(isikukood[3] + isikukood[4])
kuupaev = int(isikukood[5] + isikukood[6])

b = datetime.date.today().year
vanus = b - aasta
print("Vanus on: ",vanus,"aastat")
print("Sünnikuupäev on:",datetime.date(aasta, kuu, kuupaev))

# Kuupäev
keel = input("Vali kuupäeva keel: \n1 Eesti \n2 Inglise"":")
if keel == "1":
    kuud = ["Jaanuar","Veeburar","Märts"]
    kuupaev = datetime.date.today()
    kuu = int(kuupaev.month)
    k = datetime.date(kuupaev.year, kuu , kuupaev.day)
    print(k.strftime("%d")+". "+str(kuud[kuu-1])+" "+k.strftime("%Y"))

elif keel == "2":
    kuud = ["January","February","March"]
    kuupaev = datetime.date.today()
    kuu = int(kuupaev.month)
    k = datetime.date(kuupaev.year, kuu , kuupaev.day)
    print(k.strftime("%d")+". "+str(kuud[kuu-1])+" "+k.strftime("%Y"))