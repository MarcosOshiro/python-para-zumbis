'''
2. Sorteie 20 inteiros entre 1 e 100 numa lista.
Armazene os números pares na lista PARe os números ímpares na lista IMPAR.
Imprima as três listas.
'''
import random
lista = []
listapar = []
listaimpar = []

for x in range(20):
    a = random.randint(1, 100)
    if a not in lista:
        lista.append(a)
    if a %2 ==0:
        listapar.append(a)
    else:
        listaimpar.append(a)
    
lista.sort()
listapar.sort()
listaimpar.sort()
print (lista)
print (listapar)
print (listaimpar)
