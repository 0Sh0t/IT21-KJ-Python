'''
Kevin Joarand
Ülesanne 06
15.02.2022
'''

#

re, kesk, kokku = 0, 0, 0

#
with open('s6pru_l6ustaraamatus.txt','r') as sobrad:
    for rida in sobrad:
        enimi, pnimi,er , likes = rida.split(" ")
        print(enimi,end="")
        print(f"{enimi:11} {pnimi:11} {er:4} {likes:5}",end="")
        if er=="RE":
            re+=1
        elif er=="KE":
            kesk+=1
print("\n--------------")
print(f"Reformikad: {re}\nKesikuid: {kesk}")
print(f"Erakondi kokku: {kokku}")