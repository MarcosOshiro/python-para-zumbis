def fatorial(n):
    fat = 1
    while n >= 1:
        fat = fat * n
        n = n - 1
    return fat

'''
Para testar, no shell pode usar o comenado
for i in range(5): print (fatorial(i))

Resultado esperado
1
1
2
6
24
'''
