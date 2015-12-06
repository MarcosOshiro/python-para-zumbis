'''
Dizemos que um número natural é triangular se ele é produto de três números
naturais consecutivos.  Exemplo: 120 é triangular, pois 4.5.6 = 120.  Dado um
inteiro não-negativo n, verificar se n é triangular.
'''

n = int(input("Entre com o número: "))

a, b, c = 1, 2, 3

total = 0
while total <= n:
    if total == n:
        print("Este é um número triangular")
        break
    else:
        total = a * b * c
        a += 1
        b += 1
        c += 1
if total > n:
    print("Este não é um número triangular")


'''
Como foi resolvido no video

n = int(input('N: '))
k = 0
whilw k * (k + 1) * (k + 2) < n:
    k = k + 1

print(k * (k + 1) * (k + 2) == n)
'''
