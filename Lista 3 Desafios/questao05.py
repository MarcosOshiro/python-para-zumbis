'''
Faça um programa que peça um inteiro positivo e o mostre invertido. Ex:
1234 gera 4321
'''

n = int(input("Entre com o número: "))

inv = int(str(n)[::-1])
print (inv)

#Fiquei um tempo preso em len de int dando erro... até pensar em converter a variável... :(


'''
Como foi resolvido no video

n = input('Número: ')
n = n[::-1]
print (n)
============================
n = int(input('Número: '))
inv = 0
while n > 0:
    inv *= 10
    inv += n % 10
    n //= 10
print(inv)

'''
