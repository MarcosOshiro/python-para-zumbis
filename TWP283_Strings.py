'''
Faça um programa que leia uma palavra e troque as vogais por "*"
'''
'''
#Primeira forma de resolver
entrada = input("Entre com a palavra: ")
nova = None
nova1 = None
nova2 = None
nova3 = None
nova4 = None

nova = entrada.replace("a", "*")
nova1 = nova.replace("e", "*")
nova2 = nova1.replace("i", "*")
nova3 = nova2.replace("o", "*")
nova4 = nova3.replace("u", "*")

print (nova4)
'''

#Segunda forma de resolver
entrada = input("Entre com a palavra: ")
vogais = ["a", "e", "i", "o", "u"]
nova = ""
x = 0
y = 1
while x <= len(entrada):
    if entrada[x:y] in vogais:
        nova = nova + "*"
    else:
        nova = str(nova) + entrada[x:y]
    x += 1
    y += 1

print (nova)


'''
Como foi resolvido em video

palavra = input("Palavra: ")
k = 0
troca = ""
while k < len(palavra):
    if palavra[k] in "aeiou":
        troca = troca + "*"
    else:
        troca = troca + palavra[k]
    k += 1
print ("nova palavra %s" %troca)
'''
