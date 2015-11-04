'''
Verifique se uma palavra é palíndrome
'''
palavra = input("Entre com a palavra: ")
reverse = str(palavra[::-1])

if palavra == reverse:
    print("É um palíndrome")
else:
    print("Este não é um palíndrome")
    

'''
Como foi resolvido em video.

palavra = input ('Palavra: ')
if palavra == palavra[::-1]:
    print ('%s é palíndrome' %palavra)
else:
    print ('%s não é palíndrome' %palavra)
'''
