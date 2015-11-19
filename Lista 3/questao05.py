'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre
eles usando o algortmo de Euclides.
'''

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
resto = 1
while resto != 0:
    resto = a%b
    if resto == 0:
        print(b)
    else:
        a = b
        b = resto



