'''
Kevin Joarand
Kontrolltöö ül.3
03.14.2022
'''

import random

#Funktsioon kuvab algus teksti
def algus():
  tekst = 'Liitmine ja lahutamine'
  print('*' * len(tekst))
  print(tekst)
  print('*' * len(tekst))
  
#Funktsioon annab valida liitmis ja lahutamis tehte vahel
def tehted():
  valik = ["1. Liitmine" , "2. Lahutamine" , "3. EXIT"]
  print(valik[0])
  print(valik[1])

  
#Funktsioon vastab kasutaja sisestusele
def xsisestus():
  ksisestus = int(input("Valik: "))
  while ksisestus >  3 or ksisestus <= 0 :
    print("Sellist valikut pole")
    ksisestus = int(input("Proovi midagi muud: "))
  else:
    return ksisestus

#Funktsioon saab kasutaja vastuse
def lahendus(tehe):
  print('Sisesta vastus: ')
  print(tehe, end = '')
  tulemus  = int(input('='))
  return tulemus

#Funktsioon kontrollib kasutaja vastust
def xkontroll(KKlahendus, olahendus, k):
  if KKlahendus == olahendus:
    k += 1
    print("Õige")
    return k
  else:
    print("Väär")
    return k

#Funktsioon teeb suvaliste arvudega tehteid
def xvalik(arv, k):
  arv1 = random.randrange(1, 10)
  arv2 = random.randrange(1, 10)

  if arv is 1:
    #Genereerib liitmis tehte
    tehe  = str(arv1) + ' + ' + str(arv2)
    vastus = arv1 + arv2
    klahendus = lahendus(tehe)
    k = xkontroll(klahendus, vastus, k)
    return k
  elif arv is 2:
    #Genereerib lahutamis tehte
    tehe = str(arv1) + ' - ' + str(arv2)
    vastus = arv1 - arv2
    klahendus = lahendus(tehe)
    k = xkontroll(klahendus, vastus, k)
    return k

#Funktsioon kuvab tehete koguarvu ja õigete vastuste arvu
def tulemus(kokku, oige):
  
  if kokku > 0:
    tulemus = oige / kokku
    protsent = round((tulemus * 100), 2)
  if kokku == 0:
    protsent = 0
  print(f'Sa vastasid {kokku}-st tehtest {oige} õiget vastust')
  print(f'Sinu tulemuse protsent on: {protsent}%', sep = '')
  
def a():
  algus()
  tehted()

  o = xsisestus()
  kokku = 0
  oige = 0
  while o != 3:
    kokku += 1
    oige = xvalik(o, oige)
    o = xsisestus()
  
  print("Lõpp")
  tulemus(kokku, oige)

a()
