'''
3. Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1
e 100. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser
compostos pelos elementos intercalados dos dois outros vetores.
Imprima os três vetores.
'''
import random
lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 10:
    a = random.randint(1, 100)
    if a not in lista1:
        lista1.append(a)
while len(lista2) < 10:
    a = random.randint(1, 100)
    if a not in lista1:
        lista2.append(a)
def epar(x):
    return x%2 == 0
lista1.sort()
lista2.sort()
lista3.sort()
for x in range(10):
    if epar(x) == True:
        lista3.append(lista2[x])
    else:
        lista3.append(lista1[x])

print (lista1)
print (lista2)
print (lista3)
