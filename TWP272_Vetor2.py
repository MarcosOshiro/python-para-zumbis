'''
Faça um programa que leia um vetor de dez números reais e mostre-os na ordem inversa
'''

vetor = []
x = 0
while x < 10:
    add = float(input("Digite a posição %d: " %x))
    x += 1
    vetor.append(add)
if x == 10:
    while x <= 10:
        x -= 1
        if x < 0:
            break
        else:
            print(vetor[x])

'''
Como foi feito no video

vetor = []
i = 1
while i <= 10:
    n = float(input("Digite um número: "))
    vetor.append(n)
    i += 1
i = 9
while i >= 0:
    print (vetor[9])
    i -= 1
'''
