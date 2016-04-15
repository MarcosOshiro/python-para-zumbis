'''
Lê arquivo
'''
'''
arquivo = open('números.txt', 'r')
for linha in arquivo.readlines():
    #print(linha)
    print(linha.rstrip()) #.rstrip retira os char de controle do lado direito (r de direito)
arquivo.close()
'''

#Forma Pythonica.

with open ('números.txt') as f:
    print (f.read())
