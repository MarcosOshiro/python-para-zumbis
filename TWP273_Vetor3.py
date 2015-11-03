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

'''
Como foi resolvido no video TWP274

i = 1
while i <= 4:
	n = float(input("Nota: "))
	notas.append(n)
	i += 1
soma = 0
i = 0
while i <= 3:
	soma += notas[i]
	i += 1
print ("Notas:", notas)
print ("Média: %4.2f" %(soma/4))

'''


