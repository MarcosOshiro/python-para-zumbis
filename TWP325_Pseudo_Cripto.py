'''
Leia mensagem.txt e grave cripto.txt com todas as vogais trocadas por '*'
'''

with open ('mensagem.txt') as msg:
    entrada = msg.read()
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

    crip = open('cripto.txt', 'w')
    crip.write(nova)
    crip.close()



'''
Como foi feito no video

texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in texto.realines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
'''
