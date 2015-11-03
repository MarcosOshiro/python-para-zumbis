'''
Faça um programa que leia um vetor de 10 caracteres minúsculos, e diga quantas consoantes foram lidas.
'''

caract=[]
vogais=["a","e","i","o","u"]
vogal = 0
x = 1

while x <= 10:
    entrada = input("Caractere %d: " %x)
    x += 1
    caract.append(entrada)
for a in vogais:
    vogal += vogal

print((len(caract))-vogal)
   
