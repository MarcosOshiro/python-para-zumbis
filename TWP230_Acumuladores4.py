n = 1
soma = 0
while n <= 10:
    x = int(input('Digite o %d núnero: ' %n))
    soma = soma + x
    n = n + 1
'''
    Eu tinha feito desta forma:
    
media = soma /10
print ('Média: %d' %media)

'''

print ('Média: %5.2f' %(soma/10))
