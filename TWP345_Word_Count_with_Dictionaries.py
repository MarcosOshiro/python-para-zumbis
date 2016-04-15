'''
Faça um programa que leia o arquivo alice.txt e conte o número de ocorrências de
cada palavra no texto.  Obs.: para saber os caracteres especiais use import
string e utilize string.punctuation
'''

'''
Como tentei fazer.... Até contou direito, mas fudeu no lance de retirar as pontuações

import string
with open ('alice.txt') as livro:
    texto = livro.read()
    texto =texto.lower()
    texto = texto.replace(string.punctuation, '')#não funfou assim fdp hahahahhaha
    palavras = texto.split()
    dic={}
    for p in palavras:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] +=1

#roubei o print do video
print ('Alice aparece %s vezes' %dic['alice'])
    
'''
#Como foi feito no video

arq = open('alice.txt')
texto = arq.read()
texto = texto.lower()
import string
for c in string.punctuation:
    texto = texto.replace(c, ' ')
    texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] +=1
print ('Alice aparece %s vezes' %dic['alice'])
arq.close()

