'''
Faça um programa que leia uma palavra e troque as vogais por "*"
'''

entrada = input("Entre com a palavra: ")
vogais=["a","e","i","o","u"]

contvogal = 0
x = 1

while x <= 10:

    x += 1
    caract.append(entrada)
    if entrada in vogais:
        contvogal += 1
print ("Consoantes: ",(len(caract))-contvogal)

