'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos
calculando também a multiplicidade de cada fator.
'''



n = int(input('Entre com o número: '))

divisores = []
d = 2
while n > 1:
    if n%d == 0:
        n = n/d
        divisores.append(d)
    else:
        d += 1
print ("Estes são os divisores", divisores)

'''
Como foi feito no video

n = int(input('Número: '))
for k in range(2, n):
    while n % k == 0:
        print (k)
        n = n / k
'''


