import random

a = 0
b = 0


funktsioon=['+','-']

print('Liitmise ja lahutamise õppimine')

while a <10:
    esimenearv=random.randint(0, 10)
    teinearv=random.randint(0, 10)
    tehe=random.choice(funktsioon)

    kysimus=print(esimenearv, tehe, teinearv, '=')

    choice = input(">")


    if tehe== '+':
                    arv=esimenearv+teinearv
                    if int (choice) == esimenearv+teinearv:
                        print ('Õige')
                        b= b+1
                    else:
                        print ('Väär')
    elif tehe== '-':
                    arv=a-b
                    if int (choice) == esimenearv-teinearv:
                        print ('Õige')
                        b= b+1
                    else:
                        print ('Väär')

    a += 1

print ("Tehted said otsa")

arv = 10
print("Sa said %d õiget %d-st" % (b, arv))
percentage = round((g * 100), 2)
    if arv == 0:
    percentage = 0
  print(f'Your score is {percentage}%.', sep = '')
