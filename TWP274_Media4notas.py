'''
Faça um programa que leia um vetor de 10 caracteres minúsculos, e diga quantas consoantes foram lidas.
'''

caract=[]
vogais=["a","e","i","o","u"]
contvogal = 0
x = 1
while x <= 10:
    entrada = input("Caractere %d: " %x)
    x += 1
    caract.append(entrada)
    if entrada in vogais:
        contvogal += 1
print ("Consoantes: ",(len(caract))-contvogal)
   
'''
Como foi feito no video

letras = []
i = 1
while i <= 10:
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    if letras[1] not in 'aeiou':
        cont += 1
    i += 1
print ("Foram lidos %d consoantes" %cont)
'''
