import random
lista = []

while len(lista) < 15:
    a = random.randint(10, 100)
    if a in lista:
        a = 0
    else:
        lista.append(a)
lista.sort()
print(lista)

'''
Como foi feito no video

import random
lista = []
while len(lista < 15:
    x = random.randint(10, 100)
    if x not in lista:
        lista.append(x)
lista.sort()
print (lista)
'''
