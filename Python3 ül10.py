'''
Kevin Joarand
Ülesanne 10
08.03.2022
'''

import re
#Väljastab IP-d
i = open('ip.txt')
for line in i:
    if re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):
         print(line,end='')

#Väljastab õiged paroolid
p = open('ip.txt')
for line in p:
    if re.search('^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9[\]]+$', line):
         print(line,end='')