'''
Faça um programa que leia 4 notas, mostre as notas e a média na tela
'''
notas=[]
x = 1
soma = 0
while x <= 4:
    add = float(input("Nota %d: " %x))
    x += 1
    notas.append(add)
    soma += add
print(notas)
print("------")
print("%2.2f" %(soma/4))
