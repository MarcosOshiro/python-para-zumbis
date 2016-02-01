a = 5 #variável global
def muda_e_imprime():
    #global a >>> Assim estaríamos "chamando" a mesma variável a.
    a = 7 #variável local
    print ('a dentro da função: %d' %a)
print ('a antes de mudar: %d' %a)
muda_e_imprime()
print ('a depois de mduar: %d' %a)

'''
Resultado esperado

a antes de mudar: 5
a dentro da função: 7
a depois de mudar: 5

======
Resultado esperado chamando a variável global

a antes de mudar: 5
a dentro da função: 7
a depois de mudar: 7

'''

